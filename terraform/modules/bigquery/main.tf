provider "google" {
  project = var.project_id
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_id
  location   = var.dataset_location
}