FROM jupyter/tensorflow-notebook

# user name is Jovyan and uts user Id is NB_UID
USER $NB_UID 

RUN pip install --upgrade pip && \
    pip install transformers && \
    pip install pysrt && \
    fix-permissions "/home/${NB_USER}"
