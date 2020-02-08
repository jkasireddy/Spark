//variable "object_id" {
//  type = "string"
//  description = "object id's to assign the contributor role"
//  default = "test1"
//}

variable "object_ids" {
  type = "list"
  description = "object id's to assign the contributor role"
  default = ["test1","test2","test3"]
}

resource "azurerm_role_assignment" "vnet_roles" {
  principal_id = data.azurerm_virtual_network.test.id
  count = length(var.object_ids)
  role_definition_name = "Contributor"
  scope = var.object_ids[count.index]
}