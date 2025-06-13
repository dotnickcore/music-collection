# music-collection
# 🎵 Album & Song Management System

A simple yet powerful application for managing music albums and songs using SQLite for persistent and efficient storage.

---

## 📁 1. Album Management

### ➕ Create Album
- Allows users to create an album by specifying its name.
- ❌ **Error**: Album already exists.

### 🗑️ Delete Album
- Deletes the specified album and all its associated songs.
- ❌ **Error**: Album doesn’t exist.

---

## 🎶 2. Song Management

### ➕ Add Song
1. User inputs a song name.
2. If duplicate songs exist:
   - Displays matching songs (with name, artist, duration, genre, album).
   - Asks for confirmation to proceed.
3. If confirmed:
   - Requires album name (must exist).
   - Requires song details (name, artist, duration, genre).

#### ❌ Errors:
- Song already exists (same name, artist, duration, genre).
- Album duration limit exceeded (e.g., max 80 minutes).
- Album does not exist.
- Album is full (e.g., max 30 songs).

### 🗑️ Delete Song
- Removes a song from a specified album.

#### ❌ Error:
- Album or song doesn’t exist.

---

## 🔍 3. Query Features

All query results are **sortable** by various criteria.

### 🔎 Search by Song Name
- Lists all songs with a given name + details.
- 📌 Sortable by: `artist`, `duration`, `album`.

### 💿 List Album Contents
- Shows all songs in a specific album.
- 📌 Sortable by: `track order`, `duration`, `name`.

### 📚 List All Albums
- Displays all albums with song count and total duration.
- 📌 Sortable by: `name`, `year`, `song count`.

### ⏱️ Filter by Duration
- Lists all songs shorter than X minutes.
- 📌 Sortable by: `duration` (asc/desc).

### 🎧 Filter by Genre
- Lists all songs of a given genre.
- 📌 Sortable by: `artist`, `album`, `duration`.

### 🕳️ Empty Result Handling
- Friendly message if no results found.

---

## 📊 4. Statistics

### 📈 Collection Insights
- **Total Collection Duration**: Sum of all song durations.
- **Most Common Genre**: Genre appearing most frequently.

### 📉 Album Analytics
- Shortest and longest album by total duration.
- Average song duration per album.

---

## 🛠️ 5. SQLite-Specific Enhancements

- ✅ **Automatic Duplicate Prevention**: Unique constraint on `(song, artist, duration, genre)`.
- ⚡ **Efficient Queries**: Indexed columns for fast filtering and sorting.
- 💾 **Persistent Storage**: Uses a single `.db` file (no JSON or CSV required).
- 🔐 **Transaction Safety**: Operations like album deletion cascade to remove linked songs safely.

---

# ⚠️ Error Handling Guide

This section documents the common error messages, input validation errors, and business rule validation logic for the Album & Song Management System.

---

## ❗ Common Error Messages

| Code                  | Message                                             |
|-----------------------|-----------------------------------------------------|
| `ERR_NOT_FOUND`       | The requested resource was not found.              |
| `ERR_ALREADY_EXISTS`  | The resource already exists.                       |
| `ERR_INVALID_INPUT`   | One or more input fields are invalid.              |
| `ERR_DATABASE`        | An internal database error occurred.              |
| `ERR_OPERATION_FAILED`| The operation could not be completed. Try again.   |
| `ERR_CONFIRMATION_REQUIRED` | Confirmation required before proceeding.     |
| `ERR_NO_RESULTS`      | No results found matching the criteria.            |

---

## 🧾 Format Validation Errors

Input validation ensures that users provide data in the correct format.

| Field        | Rule                                      | Error Message                                    |
|--------------|-------------------------------------------|--------------------------------------------------|
| `albumName`  | Must be non-empty and alphanumeric        | Album name must be a non-empty string.           |
| `songName`   | Must be non-empty and alphanumeric        | Song name must be a non-empty string.            |
| `artist`     | Must be non-empty                         | Artist name cannot be empty.                     |
| `duration`   | Must be a positive number (minutes)       | Duration must be a valid number greater than 0.  |
| `genre`      | Must be from a predefined list            | Genre must be one of the allowed categories.     |
| `trackOrder` | Must be a positive integer (if applicable)| Track order must be a positive number.           |
| `year`       | Must be a 4-digit year (optional)         | Year must be in YYYY format.                     |

---

## 🧠 Business Rule Validation Errors

These rules enforce domain-specific logic beyond basic format validation.

| Scenario                                      | Error Message                                                  |
|----------------------------------------------|----------------------------------------------------------------|
| Creating a duplicate album                    | Album with the same name already exists.                      |
| Deleting a non-existent album                 | Album not found.                                              |
| Adding a song to a non-existent album         | Specified album does not exist.                               |
| Adding a duplicate song                       | This song already exists in the system.                       |
| Album duration exceeds 80 minutes             | Cannot add song. Album duration limit exceeded.               |
| Album song count exceeds 30 songs             | Cannot add song. Album is full.                               |
| Deleting a non-existent song                  | Song not found in the specified album.                        |
| Searching yields no results                   | No matching songs found.                                      |
| Genre not recognized                          | Invalid genre selected.                                       |
| Invalid sorting field                         | Cannot sort by the given key.                                 |
| Album has no songs                            | Album has no songs to display.                                |
| Duplicate song name detected (confirmation)   | Multiple songs with this name found. Please confirm details.  |

---

## ✅ Best Practices

- Always validate user inputs before performing operations.
- Use unique constraints in SQLite to prevent duplicates at the database level.
- Handle empty results gracefully with user-friendly messages.
- Confirm potentially destructive actions (e.g., deleting albums with songs).

# References:
- https://github.com/Italiant/SENG1110/tree/main
- https://github.com/Mohammed-devv/Music-Collection-Manager-Java-OOP-Project/tree/main
- https://www.youtube.com/watch?v=pd-0G0MigUA
- https://www.youtube.com/watch?v=girsuXz0yA8
