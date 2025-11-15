package main

import (
	"github.com/gofiber/fiber/v2"
)

func SetupRoutes(app *fiber.App) {
	app.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"title": "Go Fiber",
		})
	})

	// API Routes
	api := app.Group("/api")
	api.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"title": "API",
		})
	})

	// API V1 Routes
	v1 := api.Group("/v1")
	v1.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"title": "API V1",
		})
	})
}
