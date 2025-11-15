package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
	"github.com/gofiber/template/html/v2"

	"go-fiber/core"
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

	// Set HTML engine
	engine := html.New("./views", ".html")

	// Create new Fiber app
	app := fiber.New(fiber.Config{
		Views: engine,
	})

	// Setup logging
	app.Use(logger.New())

	// Setup all route endpoints
	SetupRoutes(app)

	return app
}
