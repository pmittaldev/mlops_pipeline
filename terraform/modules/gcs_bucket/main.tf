# Submodule: modules/gcs_bucket/main.tf

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "gcs_bucket" {
  name          = var.bucket_name
  location      = var.location
  storage_class = var.storage_class

  versioning {
    enabled = true
  }
}