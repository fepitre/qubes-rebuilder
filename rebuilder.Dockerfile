FROM rebuilder_base:latest
MAINTAINER Frédéric Pierret <frederic.pierret@qubes-os.org>

# REBUILDER
RUN apt-get update && apt-get install -y mmdebstrap in-toto python3-dateutil && apt-get clean all
RUN git clone https://github.com/fepitre/debrebuild /opt/debrebuild && cd /opt/debrebuild && git checkout 8864c0d974a9ad54ba7b4d939405c1055acf61f5