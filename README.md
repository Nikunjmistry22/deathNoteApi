# Death Note API Documentation

Welcome to the Death Note API! This API provides access to information about characters and episodes from the Death Note anime series.

## API Endpoints

### Get All Characters

- **Endpoint**: `/characters`
- **Method**: `GET`
- **Parameters**:
  - `page` (optional): Page number (default: 1)
  - `limit` (optional): Number of results per page (default: 10)
- **Description**: Retrieves a list of characters.
- **Example**: `GET /characters?page=1&limit=10`
- **Response**:
  ```json
  {
  "current_page": 1,
  "documents": [
    {
      "_id": "1",
      "affiliation": "N/A",
      "age": 17,
      "alias": "Kira",
      "blood_type": "A",
      "cause_of_death": "Shot",
      "date_of_birth": "1986-02-28",
      "death_date": "2010-01-28",
      "description": "Protagonist of the series.",
      "enemies": [
        {
          "name": "L"
        }
      ],
      "family_members": [
        {
          "name": "Soichiro Yagami",
          "relationship": "Father"
        }
      ],
      "first_appearance": "Episode 1",
      "friends": [
        {
          "name": "Misa Amane"
        }
      ],
      "gender": "Male",
      "height": 179,
      "image_url": "https://cdn-eu.anidb.net/images/main/231916.jpg",
      "last_appearance": "Episode 37",
      "name": "Light Yagami",
      "nationality": "Japanese",
      "notable_abilities": "Genius intellect, strategic thinking",
      "notable_quotes": [
        "I am Justice!",
        "I will become the God of the new world!"
      ],
      "occupation": "Student",
      "portrayed_by": "Tatsuya Fujiwara",
      "weight": 54
    }
  ],
  "total_pages": 3
  }

  ```
  <hr>
  
  ### Get Character by Character_Id 

- **Endpoint**: `/characters/<character_id>`
- **Method**: `GET`
- **Parameters**:
  - `page` (optional): Page number (default: 1)
  - `limit` (optional): Number of results per page (default: 10)
- **Description**: Retrieves a specific character by its id.
- **Example**: `GET /characters/1`
- **Response**:
  ```json
  {
  "_id": "1",
  "affiliation": "N/A",
  "age": 17,
  "alias": "Kira",
  "blood_type": "A",
  "cause_of_death": "Shot",
  "date_of_birth": "1986-02-28",
  "death_date": "2010-01-28",
  "description": "Protagonist of the series.",
  "enemies": [
    {
      "name": "L"
    }
  ],
  "family_members": [
    {
      "name": "Soichiro Yagami",
      "relationship": "Father"
    }
  ],
  "first_appearance": "Episode 1",
  "friends": [
    {
      "name": "Misa Amane"
    }
  ],
  "gender": "Male",
  "height": 179,
  "image_url": "https://cdn-eu.anidb.net/images/main/231916.jpg",
  "last_appearance": "Episode 37",
  "name": "Light Yagami",
  "nationality": "Japanese",
  "notable_abilities": "Genius intellect, strategic thinking",
  "notable_quotes": [
    "I am Justice!",
    "I will become the God of the new world!"
  ],
  "occupation": "Student",
  "portrayed_by": "Tatsuya Fujiwara",
  "weight": 54
  }
  ```
  <hr>
  
### Get All Episodes

- **Endpoint**: `/episodes`
- **Method**: `GET`
- **Parameters**:
  - `page` (optional): Page number (default: 1)
  - `limit` (optional): Number of results per page (default: 10)
- **Description**: Retrieves a list of characters.
- **Example**: `GET /episodes?page=2&limit=3`
- **Response**:
  ```json
  {
  "current_page": 2,
  "documents": [
    {
      "_id": "669755fc86a612c7f406acbe",
      "air_date": "2006-10-25",
      "characters": [
        {
          "id": 1,
          "name": "Light Yagami",
          "role": "Protagonist"
        },
        {
          "id": 4,
          "name": "Naomi Misora",
          "role": "FBI Agent"
        }
      ],
      "description": "Light tries to discover the name of the woman who is investigating the Kira case.",
      "duration": "22 minutes",
      "episode_number": 4,
      "id": 4,
      "season": 1,
      "title": "Pursuit"
    },
    {
      "_id": "669755fc86a612c7f406acbf",
      "air_date": "2006-11-01",
      "characters": [
        {
          "id": 1,
          "name": "Light Yagami",
          "role": "Protagonist"
        },
        {
          "id": 3,
          "name": "L",
          "role": "Detective"
        }
      ],
      "description": "The battle between Light and L continues as L's suspicions about Light's identity grow.",
      "duration": "22 minutes",
      "episode_number": 5,
      "id": 5,
      "season": 1,
      "title": "Tactics"
    },
    {
      "_id": "669755fc86a612c7f406acc0",
      "air_date": "2006-11-08",
      "characters": [
        {
          "id": 1,
          "name": "Light Yagami",
          "role": "Protagonist"
        },
        {
          "id": 3,
          "name": "L",
          "role": "Detective"
        }
      ],
      "description": "L creates a daring plan to try and expose Light as Kira.",
      "duration": "22 minutes",
      "episode_number": 6,
      "id": 6,
      "season": 1,
      "title": "Unraveling"
    }
  ],
  "total_pages": 13
  }

  ```
  <hr>
  
  ### Get Episode by Episode_Id 
- **Endpoint**: `/episodes/<episode_id>`
- **Method**: `GET`
- **Parameters**:
  - `page` (optional): Page number (default: 1)
  - `limit` (optional): Number of results per page (default: 10)
- **Description**: Retrieves a specific character by its id.
- **Example**: `GET /episodes/669755fc86a612c7f406acbe`
- **Response**:
  ```json
  {
  "_id": "669755fc86a612c7f406acbe",
  "air_date": "2006-10-25",
  "characters": [
    {
      "id": 1,
      "name": "Light Yagami",
      "role": "Protagonist"
    },
    {
      "id": 4,
      "name": "Naomi Misora",
      "role": "FBI Agent"
    }
  ],
  "description": "Light tries to discover the name of the woman who is investigating the Kira case.",
  "duration": "22 minutes",
  "episode_number": 4,
  "id": 4,
  "season": 1,
  "title": "Pursuit"
  }
  ```
  <hr>
  
