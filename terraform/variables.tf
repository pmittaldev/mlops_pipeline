# Root module: variables.tf

variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "bucket_name" {
  type = string
}

variable "location" {
  type = string
}

variable "storage_class" {
  type    = string
  default = "STANDARD"
}

variable "bigquery_dataset_id" {
  type = string
}

variable "vertex_ai_endpoint_name" {
  type = string
}
