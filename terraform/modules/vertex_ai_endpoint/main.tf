provider "google" {
  project = var.project_id
  region  = var.location
}

resource "google_vertex_ai_endpoint" "endpoint" {
  display_name = var.display_name
  location = var.location
  name = var.name
}