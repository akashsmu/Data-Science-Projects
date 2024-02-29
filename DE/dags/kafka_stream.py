from datetime import datetime
#from airflow import DAG
#from airflow.operators.python import PythonOperator

default_args = {
    'owner':'airscholar',
    'start_date': datetime(2024,3,1,10,00)
}

def get_data():
    import requests
    res = requests.get("https://randomuser.me/api/").json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    
def stream_data():
    import json
    


# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()