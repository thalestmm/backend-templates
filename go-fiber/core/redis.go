package core

import (
	"github.com/redis/go-redis/v9"
)

func RedisClient() (*redis.Client, error) {
	// Singleton Redis client

	// Load environment config
	cfg, err := LoadConfig()
	if err != nil {
		return nil, err
	}

	// Parse Redis URL from config
	opts, err := redis.ParseURL(cfg.RedisURL)
	if err != nil {
		return nil, err
	}

	return redis.NewClient(opts), nil
}
