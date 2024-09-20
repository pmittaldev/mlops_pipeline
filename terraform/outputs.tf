output "gcs_bucket_name" {
  value = module.gcs_bucket.bucket_name
}

output "bigquery_dataset_id" {
  value = module.bigquery.dataset_id
}

output "vertex_ai_endpoint_name" {
  value = module.vertex_ai_endpoint.endpoint_name
}