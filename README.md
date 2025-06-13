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

> Designed for extensibility and clean integration with a user-friendly interface or CLI.

# References:
- https://github.com/Italiant/SENG1110/tree/main
- https://github.com/Mohammed-devv/Music-Collection-Manager-Java-OOP-Project/tree/main
- https://www.youtube.com/watch?v=pd-0G0MigUA
