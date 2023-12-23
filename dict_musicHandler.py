# dict_musicHandler.py

# Data structure for the track data
max_track_amount = 32
stage_data_dict = {
    'STG00': {
        'StageName': 'Air Ship',
        'TrackFmt': 'ADX%sS000',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG01': {
        'StageName': 'Desert',
        'TrackFmt': 'ADX%sS010',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG02': {
        'StageName': 'Factory',
        'TrackFmt': 'ADX%sS020',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG03': {
        'StageName': 'Carnival',
        'TrackFmt': 'ADX%sS030',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG04': {
        'StageName': 'Swamp',
        'TrackFmt': 'ADX%sS040',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG05': {
        'StageName': 'Blue Cave',
        'TrackFmt': 'ADX%sS050',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG06': {
        'StageName': 'Clock',
        'TrackFmt': 'ADX%sS060',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG07': {
        'StageName': 'River Raft Frozen',
        'TrackFmt': 'ADX%sS070',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG08': {
        'StageName': 'Abyss',
        'TrackFmt': 'ADX%sS080',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG09': {
        'StageName': 'Alt AirShip',
        'TrackFmt': 'ADX%sNSHP',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG0A': {
        'StageName': 'Alt Desert',
        'TrackFmt': 'ADX%sNDST',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG0B': {
        'StageName': 'Training',
        'TrackFmt': 'ADX%sS0B0',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG0C': {
        'StageName': 'Alt Carnival',
        'TrackFmt': 'ADX%sNCRN',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG0D': {
        'StageName': 'Pink Swamp',
        'TrackFmt': 'ADX%sNSWP',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG0E': {
        'StageName': 'Lava Cave',
        'TrackFmt': 'ADX%sNCAV',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG0F': {
        'StageName': 'Winter Clock',
        'TrackFmt': 'ADX%sNCLK',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'STG10': {
        'StageName': 'River Raft Wooden',
        'TrackFmt': 'ADX%sNRFT',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'MODE_MENU': {
        'StageName': 'Mode Menu',
        'TrackFmt': 'ADX%sMENU',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
    'CHAR_SELC': {
        'StageName': 'Character Select',
        'TrackFmt': 'ADX%sSELC',
        'Choices': ['Choose from ADXs'] * max_track_amount,
    },
}
# Track settings with descriptions
track_settings = {
    '2 Track': {
        'TrackAmount': 2,
        'Desc': '2 Tracks per Stage',
    },
    '4 Track': {
        'TrackAmount': 4,
        'Desc': '4 Tracks per Stage',
    },
    '8 Track': {
        'TrackAmount': 8,
        'Desc': '8 Tracks per Stage',
    },
    '32 Shuffle': {
        'TrackAmount': 32,
        'Desc': '32 Tracks played randomly for all stages',
        'SpecialPlaylist': True  # Add a flag to indicate this is a special playlist
    },
}