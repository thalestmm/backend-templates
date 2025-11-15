package core

import (
	"github.com/caarlos0/env/v11"
	"github.com/joho/godotenv"
)

type Config struct {
	Environment string `env:"ENVIRONMENT" envDefault:"development"`
}

func LoadConfig() (*Config, error) {
	// Load .env file (if exists)
	_ = godotenv.Load() // Ignore error (optional .env file)

	cfg := &Config{}

	// Parse environment into the Config struct
	if err := env.Parse(cfg); err != nil {
		return nil, err
	}

	return cfg, nil
}
