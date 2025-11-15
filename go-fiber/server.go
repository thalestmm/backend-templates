package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
)

func main() {
	app := InitApp()

	log.Fatal(app.Listen(":3000"))
}

func InitApp() *fiber.App {
	// Dedicated app initialization for allowing app import for tests

	// Set HTML engine
	engine := html.New("./views", ".html")

	// Create new Fiber app
	app := fiber.New(fiber.Config{
		Views: engine,
	})

	// Setup all route endpoints
	SetupRoutes(app)

	return app
}
