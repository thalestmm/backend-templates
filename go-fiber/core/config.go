package core

import (
	"errors"

	"github.com/caarlos0/env/v11"
	"github.com/go-playground/validator/v10"
	"github.com/joho/godotenv"
)

// Config TODO: Add the remaining settings
type Config struct {
	Environment string `env:"ENVIRONMENT" envDefault:"dev" validate:"oneof=dev staging prod"`
	RedisURL    string `env:"REDIS_URL" envDefault:"redis://localhost:6379"`
}

var validate = validator.New()

func LoadConfig() (*Config, error) {
	// Load configuration from environment
	// OBS: Variables passed inside the docker-compose override the .env ones

	// Load .env file (if exists)
	_ = godotenv.Load() // Ignore error (optional .env file)

	cfg := &Config{}

	// Parse environment into the Config struct
	if err := env.Parse(cfg); err != nil {
		return nil, errors.New("config load error: " + err.Error())
	}

	// Validate the Config struct
	if err := validate.Struct(cfg); err != nil {
		return nil, errors.New("environment validation failed: " + err.Error())
	}

	return cfg, nil
}
