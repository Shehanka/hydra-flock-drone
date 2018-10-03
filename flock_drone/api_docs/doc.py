"""
Generated API Documentation for Server API using server_doc_gen.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readonly": "hydra:readonly",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "statusCode": "hydra:statusCode",
        "statusCodes": "hydra:statusCodes",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://localhost:8081/api/vocab#",
        "writeonly": "hydra:writeonly"
    },
    "@id": "http://localhost:8081/api/vocab",
    "@type": "ApiDocumentation",
    "description": "API Documentation for the drone side system",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "vocab:State",
            "@type": "hydra:Class",
            "description": "Class for drone state objects",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readonly": "true",
                    "required": "false",
                    "title": "Speed",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readonly": "true",
                    "required": "false",
                    "title": "Position",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/Property",
                    "readonly": "true",
                    "required": "false",
                    "title": "Direction",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/fuelCapacity",
                    "readonly": "true",
                    "required": "false",
                    "title": "Battery",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "https://schema.org/status",
                    "readonly": "true",
                    "required": "false",
                    "title": "Status",
                    "writeonly": "false"
                }
            ],
            "title": "State"
        },
        {
            "@id": "vocab:Drone",
            "@type": "hydra:Class",
            "description": "Class for a drone",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Drone not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Drone returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Drone",
                    "title": "GetDrone"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Drone",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Drone updated",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateDrone"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Drone",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "Drone added",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "AddDrone"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readonly": "false",
                    "required": "true",
                    "title": "State",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/name",
                    "readonly": "false",
                    "required": "true",
                    "title": "name",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/model",
                    "readonly": "false",
                    "required": "true",
                    "title": "model",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://auto.schema.org/speed",
                    "readonly": "false",
                    "required": "true",
                    "title": "MaxSpeed",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/device",
                    "readonly": "false",
                    "required": "true",
                    "title": "Sensor",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeonly": "false"
                }
            ],
            "title": "Drone"
        },
        {
            "@id": "vocab:Command",
            "@type": "hydra:Class",
            "description": "Class for drone commands",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Command not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Command Returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Command",
                    "title": "GetCommand"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Command",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "Command added",
                            "statusCode": 201
                        }
                    ],
                    "returns": "null",
                    "title": "AddCommand"
                },
                {
                    "@type": "http://schema.org/DeleteAction",
                    "expects": "null",
                    "method": "DELETE",
                    "possibleStatus": [
                        {
                            "description": "Command deleted",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "DeleteCommand"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:State",
                    "readonly": "false",
                    "required": "true",
                    "title": "State",
                    "writeonly": "false"
                }
            ],
            "title": "Command"
        },
        {
            "@id": "vocab:Datastream",
            "@type": "hydra:Class",
            "description": "Class for a data entry from drone sensors",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Datastream not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Datastream returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Datastream",
                    "title": "GetDatastream"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Datastream",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Datastream updated",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateDatastream"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Datastream",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "Datastream added",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "AddDatastream"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/QuantitativeValue",
                    "readonly": "false",
                    "required": "true",
                    "title": "Temperature",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/geo",
                    "readonly": "false",
                    "required": "true",
                    "title": "Position",
                    "writeonly": "false"
                }
            ],
            "title": "Datastream"
        },
        {
            "@id": "vocab:Anomaly",
            "@type": "hydra:Class",
            "description": "Class for Temperature anomalies that need to be confirmed",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Anomaly not found",
                            "statusCode": 404
                        },
                        {
                            "description": "Anomaly returned",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:Anomaly",
                    "title": "GetAnomaly"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Anomaly",
                    "method": "PUT",
                    "possibleStatus": [
                        {
                            "description": "Anomaly added successfully",
                            "statusCode": 201
                        }
                    ],
                    "returns": "null",
                    "title": "AddAnomaly"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Anomaly",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Anomaly updated successfully",
                            "statusCode": 201
                        }
                    ],
                    "returns": "null",
                    "title": "UpdateAnomaly"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:Location",
                    "readonly": "false",
                    "required": "true",
                    "title": "Location",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": "false",
                    "required": "true",
                    "title": "DroneID",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/eventStatus",
                    "readonly": "false",
                    "required": "true",
                    "title": "Status",
                    "writeonly": "false"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "http://schema.org/identifier",
                    "readonly": "false",
                    "required": "true",
                    "title": "AnomalyID",
                    "writeonly": "false"
                }
            ],
            "title": "Anomaly"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "vocab:CommandCollection",
            "@type": "hydra:Class",
            "description": "A collection of command",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:command_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all Command entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:CommandCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:command_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new Command entitity",
                    "expects": "vocab:Command",
                    "method": "PUT",
                    "returns": "vocab:Command",
                    "statusCodes": [
                        {
                            "description": "If the Command entity was created successfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The command",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "CommandCollection"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "http://schema.org/FindAction",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "null",
                    "statusCodes": "vocab:EntryPoint"
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The Drone Class",
                    "hydra:title": "drone",
                    "property": {
                        "@id": "vocab:EntryPoint/Drone",
                        "@type": "hydra:Link",
                        "description": "Class for a drone",
                        "domain": "vocab:EntryPoint",
                        "label": "Drone",
                        "range": "vocab:Drone",
                        "supportedOperation": [
                            {
                                "@id": "getdrone",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetDrone",
                                "method": "GET",
                                "returns": "vocab:Drone",
                                "statusCodes": [
                                    {
                                        "description": "Drone not found",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "Drone returned",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "updatedrone",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:Drone",
                                "label": "UpdateDrone",
                                "method": "POST",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Drone updated",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "adddrone",
                                "@type": "http://schema.org/AddAction",
                                "description": "null",
                                "expects": "vocab:Drone",
                                "label": "AddDrone",
                                "method": "PUT",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Drone added",
                                        "statusCode": 200
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The Datastream Class",
                    "hydra:title": "datastream",
                    "property": {
                        "@id": "vocab:EntryPoint/Datastream",
                        "@type": "hydra:Link",
                        "description": "Class for a data entry from drone sensors",
                        "domain": "vocab:EntryPoint",
                        "label": "Datastream",
                        "range": "vocab:Datastream",
                        "supportedOperation": [
                            {
                                "@id": "getdatastream",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetDatastream",
                                "method": "GET",
                                "returns": "vocab:Datastream",
                                "statusCodes": [
                                    {
                                        "description": "Datastream not found",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "Datastream returned",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "updatedatastream",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:Datastream",
                                "label": "UpdateDatastream",
                                "method": "POST",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Datastream updated",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "adddatastream",
                                "@type": "http://schema.org/AddAction",
                                "description": "null",
                                "expects": "vocab:Datastream",
                                "label": "AddDatastream",
                                "method": "PUT",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Datastream added",
                                        "statusCode": 200
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The Anomaly Class",
                    "hydra:title": "anomaly",
                    "property": {
                        "@id": "vocab:EntryPoint/Anomaly",
                        "@type": "hydra:Link",
                        "description": "Class for Temperature anomalies that need to be confirmed",
                        "domain": "vocab:EntryPoint",
                        "label": "Anomaly",
                        "range": "vocab:Anomaly",
                        "supportedOperation": [
                            {
                                "@id": "getanomaly",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "null",
                                "label": "GetAnomaly",
                                "method": "GET",
                                "returns": "vocab:Anomaly",
                                "statusCodes": [
                                    {
                                        "description": "Anomaly not found",
                                        "statusCode": 404
                                    },
                                    {
                                        "description": "Anomaly returned",
                                        "statusCode": 200
                                    }
                                ]
                            },
                            {
                                "@id": "addanomaly",
                                "@type": "http://schema.org/AddAction",
                                "description": "null",
                                "expects": "vocab:Anomaly",
                                "label": "AddAnomaly",
                                "method": "PUT",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Anomaly added successfully",
                                        "statusCode": 201
                                    }
                                ]
                            },
                            {
                                "@id": "updateanomaly",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:Anomaly",
                                "label": "UpdateAnomaly",
                                "method": "POST",
                                "returns": "null",
                                "statusCodes": [
                                    {
                                        "description": "Anomaly updated successfully",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The CommandCollection collection",
                    "hydra:title": "commandcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/CommandCollection",
                        "@type": "hydra:Link",
                        "description": "The CommandCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "CommandCollection",
                        "range": "vocab:CommandCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:command_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all Command entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:CommandCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:command_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new Command entitity",
                                "expects": "vocab:Command",
                                "method": "PUT",
                                "returns": "vocab:Command",
                                "statusCodes": [
                                    {
                                        "description": "If the Command entity was created successfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "API Doc for the drone side API"
}
