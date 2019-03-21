# Django-Rest-API

This project is based on Django REST API framework.  

## API - Recipes

```
BASE_URL: '/api/recipes/'
```

#### To get all recipes

```
Url : BASE_URL
Request Method: GET
Response Format:

{
    "data": [
        {
            "id": 2,
            "name": "demo123",
            "steps": [],
            "ingredients": [],
            "user": 1
        },
        {
            "id": 10,
            "name": "demo",
            "steps": [
                {
                    "step_text": "wash onions"
                },
                {
                    "step_text": "cut onions"
                }
            ],
            "ingredients": [
                {
                    "name": "tomatos"
                },
                {
                    "name": "onions"
                }
            ],
            "user": 1
        }   
    ]
}
```

#### Add Recipe

```
Url: BASE_URL 
Request Method: POST
Request Data Format:

{
	"recipe" : {
		"name" : "(Text)",
		"steps" : [
			{
				"step_text" : "(Text)"
			},
			{
				"step_text" : "(Text)"
			}
		],
		"ingredients" : [
			{
				"name" : "(Text)"
			}
		]
	},
	"user_id" : <integer> (user should be exists in database)
}

Response Format:

{
    "data": {
        "id": 10, 
        "name": "demo",
        "steps": [
            {
                "step_text": "wash onions"
            },
            {
                "step_text": "cut onions"
            }
        ],
        "ingredients": [
            {
                "name": "tomatos"
            },
            {
                "name": "onions"
            }
        ],
        "user": 1
    }
}
```

#### Delete Recipe

```
Url: BASE_URL + '<recipe_id>'
Request Method: DELETE
<recipe_id> should exists in database
```

#### Update Recipe

```
Url: BASE_URL + '<recipe_id>'
Request Method: PUT
<recipe_id> should exists in database

```

#### Get Recipe by Id

```
Url : BASE_URL + '<recipe_id>'
Request Method: GET
```

#### Get All User Recipe

```
Url: BASE_URL + 'users/<user_id>'
Request Method: GET
<user_id> should exists in database
```



