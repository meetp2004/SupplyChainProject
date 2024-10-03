terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "supplychain-437321"
}

resource "google_storage_bucket" "static" {
  name = "supplydata"
  location = "US"
  storage_class = "STANDARD"

  force_destroy = true
}