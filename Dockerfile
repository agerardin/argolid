# FROM python:3.9
FROM polusai/bfio:2.1.9

ENV EXEC_DIR="/opt/executables"
ENV DATA_DIR="/data"
ENV POLUS_EXT=".ome.tif"

WORKDIR ${EXEC_DIR}

RUN pip3 install argolid typer==0.9

COPY ./src/python/container ${EXEC_DIR}/container

ENTRYPOINT ["python3", "-m", "container"]
CMD ["--help"]
