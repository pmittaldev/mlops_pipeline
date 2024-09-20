variable "project_id" {
  type = string
}

variable "location" {
  description = "The region where the Vertex AI endpoint will be created"
  type        = string
}

variable "display_name" {
  description = "The name of the Vertex AI endpoint"
  type        = string
}

variable "name" {
  description = "The name of the Vertex AI"
  type        = string
}
