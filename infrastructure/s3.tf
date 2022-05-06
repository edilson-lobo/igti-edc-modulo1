resource "aws_s3_bucket" "dl" {
  # Parametros de configuração do recurso escolhido
  bucket = "datalake-elobo-igti-edc-tf"
  acl    = "private"

  tags = {
      IES = "IGTI",
      CURSO = "EDC"
  }


  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}


resource "aws_s3_bucket" "stream" {
  # Parametros de configuração do recurso escolhido
  bucket = "igti-elobo-streaming-bucket"
  acl    = "private"

  tags = {
      IES = "IGTI",
      CURSO = "EDC"
  }


  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
} 