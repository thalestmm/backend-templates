package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	// Setup all route endpoints
	SetupRoutes(app)

	log.Fatal(app.Listen(":3000"))
}
