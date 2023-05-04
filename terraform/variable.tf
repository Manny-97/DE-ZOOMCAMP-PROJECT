variable "aws_region" {
  description = "The AWS region to use to create resources."
  default     = "us-east-1"
}

variable "bucket_prefix" {
    type        = string
    description = "(required since we are not using 'bucket') Creates a unique bucket name beginning with the specified prefix. Conflicts with bucket."
    default     = "bucket_name"
}

variable "tags" {
    type        = map
    description = "(Optional) A mapping of tags to assign to the bucket."
    default     = {
        environment = "DEV"
        terraform   = "true"
    }
}

variable "versioning" {
    type        = bool
    description = "(Optional) A state of versioning."
    default     = true
}

variable "acl" {
    type        = string
    description = " Defaults to private "
    default     = "private"
}

variable "aws_access_key" {
    type        = string
    description = " ACCESS KEY ID "
    default     = "value"
}

variable "aws_secret_key" {
    type        = string
    description = " SECRET KEY PASSWORD "
    default     = "value"
}
