# 🏴‍☠️ ONE PIECE TRADING PLATFORM - JAVA SPRING BOOT DOCKERFILE
# Enterprise Docker configuration like Netflix/Amazon

# Use official OpenJDK 17 image (Enterprise standard)
FROM openjdk:17-jdk-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy Maven wrapper and pom.xml first (for better caching)
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .

# Make Maven wrapper executable
RUN chmod +x ./mvnw

# Download dependencies (cached layer)
RUN ./mvnw dependency:go-offline -B

# Copy source code
COPY src src

# Build the application
RUN ./mvnw clean package -DskipTests

# Create non-root user for security
RUN groupadd -r onepiece && useradd -r -g onepiece onepiece

# Create logs directory
RUN mkdir -p /var/log/onepiece-trading && \
    chown -R onepiece:onepiece /var/log/onepiece-trading

# Switch to non-root user
USER onepiece

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8080/api/actuator/health || exit 1

# Set JVM options for production
ENV JAVA_OPTS="-Xmx512m -Xms256m -XX:+UseG1GC -XX:+UseContainerSupport"

# Run the application
CMD ["sh", "-c", "java $JAVA_OPTS -jar target/onepiece-trading-platform-1.0.0.jar"]
