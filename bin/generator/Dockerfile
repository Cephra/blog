FROM alpine AS go
RUN <<EOF
wget "https://go.dev/dl/go1.22.2.linux-amd64.tar.gz"
tar -C /usr/local -xzf "go1.22.2.linux-amd64.tar.gz"
EOF

FROM alpine AS hugo
ARG HUGO_VERSION="0.125.5"
RUN <<EOF
wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
tar xf "hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
mv ./hugo /usr/bin/hugo
EOF

# Use an official Python runtime as our base image
FROM python:3-slim AS builder
RUN <<EOF
apt-get update apt-get install -y --no-install-recommends build-essential gcc
python -m venv /opt/venv
EOF
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

COPY ./requirements.txt /app

# Install any needed packages using pip
RUN pip install --no-cache -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

FROM python:3-slim AS runner

WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /opt/venv /opt/venv
COPY --from=go /usr/local/go /usr/local/go
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF
COPY --from=hugo /usr/bin/hugo /usr/bin/hugo

ENV PATH="/opt/venv/bin:$PATH:/usr/local/go/bin"

# Run command when container starts
RUN ["python"]