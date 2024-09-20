output "endpoint_name" {
  description = "The display name of the Vertex AI endpoint"
  value       = google_vertex_ai_endpoint.endpoint.display_name
}

output "endpoint_location" {
  description = "The location (region) of the Vertex AI endpoint"
  value       = google_vertex_ai_endpoint.endpoint.location
}
