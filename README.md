# Spotify Artist Discography Playlist Creator

A Python script that creates a Spotify playlist containing all albums from a specified artist.

## Description

This script allows you to:
1. Search for an artist on Spotify
2. Select the correct artist from search results
3. Automatically create a playlist containing all tracks from their albums in chronological order

## Prerequisites

- Python 3.x
- A Spotify Developer account
- The following Python packages:
  - `spotipy`
  - `python-dotenv`

## Setup

1. Create a Spotify Developer account at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application in the dashboard
3. Get your Client ID and Client Secret
4. Set up your `.env` file with the following variables:

SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=your_redirect_uri_here

## Installation

pip install spotipy python-dotenv

## Usage

1. Run the script:

python playlists.py

2. Enter the name of the artist when prompted
3. Select the correct artist from the list of results
4. Wait while the script creates your playlist and adds all tracks

## Features

- Comprehensive artist search
- Pagination support for artists with many results
- Chronological album ordering
- Handles large discographies by adding tracks in batches
- Creates a public playlist in your Spotify account

## Notes

- The script only includes official albums (not singles or EPs)
- The playlist will be created as public by default
- Track limits are handled automatically (Spotify's API limit of 100 tracks per request)
