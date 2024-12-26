FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt

COPY image/src/* ${LAMBDA_TASK_ROOT}

CMD [ "get_eigen_things.lambda_handler" ]