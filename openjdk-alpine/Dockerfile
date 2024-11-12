# Stage: build
FROM maven:3.9 AS build

WORKDIR /app

COPY pom.xml .
RUN mvn dependency:go-offline -B

COPY src ./src
RUN mvn package -DskipTests

# Stage: runtime
FROM openjdk:24-slim
LABEL maintainer="Rafa Munoz"

ENV PORT=8080 \
    APP_HOME=/app \
    JAVA_OPTS=""

EXPOSE ${PORT}
WORKDIR ${APP_HOME}

RUN addgroup --system appuser && adduser --system --no-create-home appuser --ingroup appuser

COPY --from=build /app/target/*.jar /app/app.jar
USER appuser

CMD ["/bin/sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]
