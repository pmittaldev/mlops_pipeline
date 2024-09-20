# Root module: main.tf

provider "google" {
  project = var.project_id
  region  = var.region
}

module "gcs_bucket" {
  source        = "./modules/gcs_bucket"
  project_id    = var.project_id
  region        = var.region
  bucket_name   = var.bucket_name
  location      = var.location
  storage_class = var.storage_class
}

module "bigquery" {
  source        = "./modules/bigquery"
  project_id    = var.project_id
  dataset_id    = var.bigquery_dataset_id
  dataset_location = var.location
}

module "vertex_ai_endpoint" {
  source        = "./modules/vertex_ai_endpoint"
  project_id    = var.project_id
  display_name = var.vertex_ai_endpoint_name
  location      = var.location
  name = var.vertex_ai_endpoint_name
}
