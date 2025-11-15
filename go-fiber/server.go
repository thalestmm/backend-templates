package main

import (
	"log"
	"log/slog"

	"go-fiber/core"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
)

func main() {
	app := InitApp()

	log.Fatal(app.Listen(":3000"))
}

func InitApp() *fiber.App {
	// Dedicated app initialization for allowing app import for tests

	// Load environment variables
	cfg, err := core.LoadConfig()
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Environment:", cfg.Environment)

	// Connect to Redis
	_, err = core.RedisClient() // TODO: Use the Redis client
	if err != nil {
		slog.Warn("Failed to connect to redis: " + err.Error())
	} else {
		slog.Info("Redis connection established")
	}

	// Create new Fiber app
	app := fiber.New(fiber.Config{})

	// Setup logging
	app.Use(logger.New())

	// Setup all route endpoints
	SetupRoutes(app)

	return app
}
