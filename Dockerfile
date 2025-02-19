# 使用官方的 Python 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制 Odoo 源码到工作目录
COPY . .

# 安装必要的编译工具和依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsasl2-dev \
    python3-dev \
    libldap2-dev \
    libssl-dev \
    build-essential

# 安装 Odoo 依赖
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# 安装 PostgreSQL 客户端库
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client && rm -rf /var/lib/apt/lists/*

# 设置 Odoo 配置文件路径
ENV ODOO_CONFIG=/app/odoo.config

# 暴露 Odoo 默认端口
EXPOSE 8069

# 启动 Odoo 服务
CMD ["./odoo-bin", "-c", "/app/odoo.conf"]