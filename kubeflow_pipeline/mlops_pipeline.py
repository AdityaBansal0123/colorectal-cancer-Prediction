import kfp
from kfp import dsl

def data_processing_op():
    return dsl.ContainerOp(
        name="Data Processing",
        image="bansaladitya048/cancer-colorectal:latest",
        command = ["python","src/data_precessing.py"],
    )

def model_training_op():
    return dsl.ContainerOp(
        name="Model Training",
        image="bansaladitya048/cancer-colorectal:latest",
        command = ["python","src/model_training.py"],
    )


## Pipeline starts here...

@dsl.pipeline(
    name="MLOPS Pipeline",
    description="This is my first ever kuberflow pipeline"
)
def mlops_pipeline():
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)

### RUN
if __name__=="__main__":
    kfp.compiler.Compiler().compile(
        mlops_pipeline,"mlops_pipeline.yaml"
    )