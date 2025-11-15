package main

import (
	"github.com/ansrivas/fiberprometheus/v2"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/healthcheck"
)

func SetupRoutes(app *fiber.App) {
	// Root
	app.Get("/", func(c *fiber.Ctx) error {
		return c.JSON(fiber.Map{
			"title": "Go Fiber",
		})
	})

	// Health endpoints (/livez and /readyz)
	app.Use(healthcheck.New())

	// Metrics with Prometheus
	prometheus := fiberprometheus.New("Fiber") // TODO: Change service name
	prometheus.RegisterAt(app, "/metrics")
	prometheus.SetSkipPaths([]string{"/ping", "/livez", "/readyz"}) // Remove these paths from the metrics
	prometheus.SetIgnoreStatusCodes([]int{401, 403, 404})           // Remove these status codes from the metrics
	app.Use(prometheus.Middleware)

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

	// 404 to match all other routes
	app.Use(func(c *fiber.Ctx) error {
		return c.Render("404", fiber.Map{})
	})
}
