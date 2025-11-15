# Initial builder image
FROM golang:1.25-bookworm AS build

RUN mkdir /app

WORKDIR /app

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

# Build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o /go/bin/app .

RUN chmod 0555 /go/bin/app

# Leaner runner image
FROM alpine:latest AS release

WORKDIR /app

COPY --from=build /etc/passwd /etc/passwd

COPY --from=build /go/bin/app ./main

EXPOSE 3000

CMD ["./main"]