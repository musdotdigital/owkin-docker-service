from flask import Flask

from .schemas import BackendType

EXPERIMENT_SUMMARIES = 'experiment_summaries'

app = Flask(__name__)

app.config['BACKEND_TYPE'] = BackendType.LOCAL_DOCKER
