from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "data-opentlc-221026-1025220557",
}

dag = DAG(
    "data-opentlc-221026-1025220557",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using data-opentlc-221026.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d = NotebookOp(
    name="start_spark_cluster",
    namespace="ml-workshop",
    task_id="start_spark_cluster",
    notebook="ml-workshop/src/automation/deploy_spark_jobs/start-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="data-opentlc-221026-1025220557",
    cos_dependencies_archive="start-spark-cluster-d5009697-771e-4f71-bc20-e52d905c9f9d.tar.gz",
    pipeline_outputs=["spark-info.txt"],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.8",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "SPARK_CLUSTER": "opentlc-mgr-cluster",
        "WORKER_NODES": "2",
        "S3_ENDPOINT_URL": "http://minio-ml-workshop:9000",
    },
    config_file="None",
    dag=dag,
)

notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d.image_pull_policy = "IfNotPresent"


notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51 = NotebookOp(
    name="Merge_Data",
    namespace="ml-workshop",
    task_id="Merge_Data",
    notebook="ml-workshop/src/notebooks/Merge_Data.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="data-opentlc-221026-1025220557",
    cos_dependencies_archive="Merge_Data-91a3738b-783b-4eb6-823c-1b8b013a4d51.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="quay.io/ml-aml-workshop/elyra-spark:0.0.4",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "SPARK_CLUSTER": "opentlc-mgr-cluster",
        "WORKER_NODES": "2",
        "S3_ENDPOINT_URL": "http://minio-ml-workshop:9000",
    },
    config_file="None",
    dag=dag,
)

notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51.image_pull_policy = "IfNotPresent"

(
    notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51
    << notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d
)


notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f = NotebookOp(
    name="stop_spark_cluster",
    namespace="ml-workshop",
    task_id="stop_spark_cluster",
    notebook="ml-workshop/src/automation/deploy_spark_jobs/stop-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="data-opentlc-221026-1025220557",
    cos_dependencies_archive="stop-spark-cluster-b6d6a9d3-65b6-4ef6-9ce8-4d713bea5e2f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.8",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f.image_pull_policy = "IfNotPresent"

(
    notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f
    << notebook_op_91a3738b_783b_4eb6_823c_1b8b013a4d51
)
