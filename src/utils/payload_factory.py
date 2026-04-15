
def create_product_payload(product_type_id, section_name, unique_name, status, support_type, external_se):
    return {
        "id": product_type_id,
        "name": section_name,
        "localizedName": section_name,
        "products": [
            {
                "id": None,
                "name": f"product_{unique_name}",
                "productCode": f"code_{unique_name}",
                "status": {"id": status["id"], "name": status["name"]},
                "supportType": {
                    "id": support_type["id"],
                    "name": support_type["name"],
                    "localizedName": support_type["localizedName"],
                    "wikiUrl": support_type.get("wikiUrl")
                },
                "owner": {
                    "id": None, "firstName": None, "lastName": None, "login": None,
                    "phone": None, "email": None, "telegram": None, "role": None
                },
                "externalSupportEmployee": {
                    "id": external_se["id"],
                    "firstName": external_se["firstName"],
                    "lastName": external_se["lastName"],
                    "login": external_se["login"],
                    "phone": external_se["phone"],
                    "email": external_se["email"],
                    "telegram": external_se.get("telegram"),
                    "role": external_se.get("role", {"id": None, "name": None})
                },
                "jiraUrl": None, "wikiUrl": None, "sharepointUrl": None,
                "description": None, "repositoryCodes": None
            }
        ]
    }