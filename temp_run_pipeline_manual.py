from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path

if __name__ == '__main__':
    project_path = Path.cwd()
    bootstrap_project(project_path)
    with KedroSession.create(project_path) as session:
        session.run(pipeline_name='procesamiento_de_datos')
