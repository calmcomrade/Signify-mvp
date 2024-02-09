def individual_serial(sign) -> dict:
    return {
        "id": str(sign["_id"]),
        "sign_name": str(sign["sign_name"]),
        "video_url": str(sign["video_url"]),
        "frame0": {
            "nose": {
                "x": float(sign["frame0"]["nose"]["x"]), 
                "y": float(sign["frame0"]["nose"]["y"]), 
                "z": float(sign["frame0"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame0"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame0"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame0"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame0"]["left_eye"]["x"]), 
                "y": float(sign["frame0"]["left_eye"]["y"]), 
                "z": float(sign["frame0"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame0"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame0"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame0"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame0"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame0"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame0"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame0"]["right_eye"]["x"]), 
                "y": float(sign["frame0"]["right_eye"]["y"]), 
                "z": float(sign["frame0"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame0"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame0"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame0"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame0"]["left_ear"]["x"]), 
                "y": float(sign["frame0"]["left_ear"]["y"]), 
                "z": float(sign["frame0"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame0"]["right_ear"]["x"]), 
                "y": float(sign["frame0"]["right_ear"]["y"]), 
                "z": float(sign["frame0"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame0"]["mouth_left"]["x"]), 
                "y": float(sign["frame0"]["mouth_left"]["y"]), 
                "z": float(sign["frame0"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame0"]["mouth_right"]["x"]), 
                "y": float(sign["frame0"]["mouth_right"]["y"]), 
                "z": float(sign["frame0"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame0"]["left_shoulder"]["x"]), 
                "y": float(sign["frame0"]["left_shoulder"]["y"]), 
                "z": float(sign["frame0"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame0"]["right_shoulder"]["x"]), 
                "y": float(sign["frame0"]["right_shoulder"]["y"]), 
                "z": float(sign["frame0"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame0"]["left_elbow"]["x"]), 
                "y": float(sign["frame0"]["left_elbow"]["y"]), 
                "z": float(sign["frame0"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame0"]["right_elbow"]["x"]), 
                "y": float(sign["frame0"]["right_elbow"]["y"]), 
                "z": float(sign["frame0"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame0"]["left_wrist"]["x"]), 
                "y": float(sign["frame0"]["left_wrist"]["y"]), 
                "z": float(sign["frame0"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame0"]["right_wrist"]["x"]), 
                "y": float(sign["frame0"]["right_wrist"]["y"]), 
                "z": float(sign["frame0"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame0"]["left_pinky"]["x"]), 
                "y": float(sign["frame0"]["left_pinky"]["y"]), 
                "z": float(sign["frame0"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame0"]["right_pinky"]["x"]), 
                "y": float(sign["frame0"]["right_pinky"]["y"]), 
                "z": float(sign["frame0"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame0"]["left_index"]["x"]), 
                "y": float(sign["frame0"]["left_index"]["y"]), 
                "z": float(sign["frame0"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame0"]["right_index"]["x"]), 
                "y": float(sign["frame0"]["right_index"]["y"]), 
                "z": float(sign["frame0"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame0"]["left_thumb"]["x"]), 
                "y": float(sign["frame0"]["left_thumb"]["y"]), 
                "z": float(sign["frame0"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame0"]["right_thumb"]["x"]), 
                "y": float(sign["frame0"]["right_thumb"]["y"]), 
                "z": float(sign["frame0"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame0"]["left_hip"]["x"]), 
                "y": float(sign["frame0"]["left_hip"]["y"]), 
                "z": float(sign["frame0"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame0"]["right_hip"]["x"]), 
                "y": float(sign["frame0"]["right_hip"]["y"]), 
                "z": float(sign["frame0"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame0"]["left_knee"]["x"]), 
                "y": float(sign["frame0"]["left_knee"]["y"]), 
                "z": float(sign["frame0"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame0"]["right_knee"]["x"]), 
                "y": float(sign["frame0"]["right_knee"]["y"]), 
                "z": float(sign["frame0"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame0"]["left_ankle"]["x"]), 
                "y": float(sign["frame0"]["left_ankle"]["y"]), 
                "z": float(sign["frame0"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame0"]["right_ankle"]["x"]), 
                "y": float(sign["frame0"]["right_ankle"]["y"]), 
                "z": float(sign["frame0"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame0"]["left_heel"]["x"]), 
                "y": float(sign["frame0"]["left_heel"]["y"]), 
                "z": float(sign["frame0"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame0"]["right_heel"]["x"]), 
                "y": float(sign["frame0"]["right_heel"]["y"]), 
                "z": float(sign["frame0"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame0"]["left_foot_index"]["x"]), 
                "y": float(sign["frame0"]["left_foot_index"]["y"]), 
                "z": float(sign["frame0"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame0"]["right_foot_index"]["x"]), 
                "y": float(sign["frame0"]["right_foot_index"]["y"]), 
                "z": float(sign["frame0"]["right_foot_index"]["z"])
            },
        },
                "frame1": {
            "nose": {
                "x": float(sign["frame1"]["nose"]["x"]), 
                "y": float(sign["frame1"]["nose"]["y"]), 
                "z": float(sign["frame1"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame1"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame1"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame1"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame1"]["left_eye"]["x"]), 
                "y": float(sign["frame1"]["left_eye"]["y"]), 
                "z": float(sign["frame1"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame1"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame1"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame1"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame1"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame1"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame1"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame1"]["right_eye"]["x"]), 
                "y": float(sign["frame1"]["right_eye"]["y"]), 
                "z": float(sign["frame1"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame1"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame1"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame1"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame1"]["left_ear"]["x"]), 
                "y": float(sign["frame1"]["left_ear"]["y"]), 
                "z": float(sign["frame1"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame1"]["right_ear"]["x"]), 
                "y": float(sign["frame1"]["right_ear"]["y"]), 
                "z": float(sign["frame1"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame1"]["mouth_left"]["x"]), 
                "y": float(sign["frame1"]["mouth_left"]["y"]), 
                "z": float(sign["frame1"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame1"]["mouth_right"]["x"]), 
                "y": float(sign["frame1"]["mouth_right"]["y"]), 
                "z": float(sign["frame1"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame1"]["left_shoulder"]["x"]), 
                "y": float(sign["frame1"]["left_shoulder"]["y"]), 
                "z": float(sign["frame1"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame1"]["right_shoulder"]["x"]), 
                "y": float(sign["frame1"]["right_shoulder"]["y"]), 
                "z": float(sign["frame1"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame1"]["left_elbow"]["x"]), 
                "y": float(sign["frame1"]["left_elbow"]["y"]), 
                "z": float(sign["frame1"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame1"]["right_elbow"]["x"]), 
                "y": float(sign["frame1"]["right_elbow"]["y"]), 
                "z": float(sign["frame1"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame1"]["left_wrist"]["x"]), 
                "y": float(sign["frame1"]["left_wrist"]["y"]), 
                "z": float(sign["frame1"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame1"]["right_wrist"]["x"]), 
                "y": float(sign["frame1"]["right_wrist"]["y"]), 
                "z": float(sign["frame1"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame1"]["left_pinky"]["x"]), 
                "y": float(sign["frame1"]["left_pinky"]["y"]), 
                "z": float(sign["frame1"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame1"]["right_pinky"]["x"]), 
                "y": float(sign["frame1"]["right_pinky"]["y"]), 
                "z": float(sign["frame1"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame1"]["left_index"]["x"]), 
                "y": float(sign["frame1"]["left_index"]["y"]), 
                "z": float(sign["frame1"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame1"]["right_index"]["x"]), 
                "y": float(sign["frame1"]["right_index"]["y"]), 
                "z": float(sign["frame1"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame1"]["left_thumb"]["x"]), 
                "y": float(sign["frame1"]["left_thumb"]["y"]), 
                "z": float(sign["frame1"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame1"]["right_thumb"]["x"]), 
                "y": float(sign["frame1"]["right_thumb"]["y"]), 
                "z": float(sign["frame1"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame1"]["left_hip"]["x"]), 
                "y": float(sign["frame1"]["left_hip"]["y"]), 
                "z": float(sign["frame1"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame1"]["right_hip"]["x"]), 
                "y": float(sign["frame1"]["right_hip"]["y"]), 
                "z": float(sign["frame1"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame1"]["left_knee"]["x"]), 
                "y": float(sign["frame1"]["left_knee"]["y"]), 
                "z": float(sign["frame1"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame1"]["right_knee"]["x"]), 
                "y": float(sign["frame1"]["right_knee"]["y"]), 
                "z": float(sign["frame1"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame1"]["left_ankle"]["x"]), 
                "y": float(sign["frame1"]["left_ankle"]["y"]), 
                "z": float(sign["frame1"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame1"]["right_ankle"]["x"]), 
                "y": float(sign["frame1"]["right_ankle"]["y"]), 
                "z": float(sign["frame1"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame1"]["left_heel"]["x"]), 
                "y": float(sign["frame1"]["left_heel"]["y"]), 
                "z": float(sign["frame1"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame1"]["right_heel"]["x"]), 
                "y": float(sign["frame1"]["right_heel"]["y"]), 
                "z": float(sign["frame1"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame1"]["left_foot_index"]["x"]), 
                "y": float(sign["frame1"]["left_foot_index"]["y"]), 
                "z": float(sign["frame1"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame1"]["right_foot_index"]["x"]), 
                "y": float(sign["frame1"]["right_foot_index"]["y"]), 
                "z": float(sign["frame1"]["right_foot_index"]["z"])
            },
        },
                "frame2": {
            "nose": {
                "x": float(sign["frame2"]["nose"]["x"]), 
                "y": float(sign["frame2"]["nose"]["y"]), 
                "z": float(sign["frame2"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame2"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame2"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame2"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame2"]["left_eye"]["x"]), 
                "y": float(sign["frame2"]["left_eye"]["y"]), 
                "z": float(sign["frame2"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame2"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame2"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame2"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame2"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame2"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame2"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame2"]["right_eye"]["x"]), 
                "y": float(sign["frame2"]["right_eye"]["y"]), 
                "z": float(sign["frame2"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame2"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame2"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame2"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame2"]["left_ear"]["x"]), 
                "y": float(sign["frame2"]["left_ear"]["y"]), 
                "z": float(sign["frame2"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame2"]["right_ear"]["x"]), 
                "y": float(sign["frame2"]["right_ear"]["y"]), 
                "z": float(sign["frame2"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame2"]["mouth_left"]["x"]), 
                "y": float(sign["frame2"]["mouth_left"]["y"]), 
                "z": float(sign["frame2"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame2"]["mouth_right"]["x"]), 
                "y": float(sign["frame2"]["mouth_right"]["y"]), 
                "z": float(sign["frame2"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame2"]["left_shoulder"]["x"]), 
                "y": float(sign["frame2"]["left_shoulder"]["y"]), 
                "z": float(sign["frame2"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame2"]["right_shoulder"]["x"]), 
                "y": float(sign["frame2"]["right_shoulder"]["y"]), 
                "z": float(sign["frame2"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame2"]["left_elbow"]["x"]), 
                "y": float(sign["frame2"]["left_elbow"]["y"]), 
                "z": float(sign["frame2"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame2"]["right_elbow"]["x"]), 
                "y": float(sign["frame2"]["right_elbow"]["y"]), 
                "z": float(sign["frame2"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame2"]["left_wrist"]["x"]), 
                "y": float(sign["frame2"]["left_wrist"]["y"]), 
                "z": float(sign["frame2"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame2"]["right_wrist"]["x"]), 
                "y": float(sign["frame2"]["right_wrist"]["y"]), 
                "z": float(sign["frame2"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame2"]["left_pinky"]["x"]), 
                "y": float(sign["frame2"]["left_pinky"]["y"]), 
                "z": float(sign["frame2"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame2"]["right_pinky"]["x"]), 
                "y": float(sign["frame2"]["right_pinky"]["y"]), 
                "z": float(sign["frame2"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame2"]["left_index"]["x"]), 
                "y": float(sign["frame2"]["left_index"]["y"]), 
                "z": float(sign["frame2"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame2"]["right_index"]["x"]), 
                "y": float(sign["frame2"]["right_index"]["y"]), 
                "z": float(sign["frame2"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame2"]["left_thumb"]["x"]), 
                "y": float(sign["frame2"]["left_thumb"]["y"]), 
                "z": float(sign["frame2"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame2"]["right_thumb"]["x"]), 
                "y": float(sign["frame2"]["right_thumb"]["y"]), 
                "z": float(sign["frame2"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame2"]["left_hip"]["x"]), 
                "y": float(sign["frame2"]["left_hip"]["y"]), 
                "z": float(sign["frame2"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame2"]["right_hip"]["x"]), 
                "y": float(sign["frame2"]["right_hip"]["y"]), 
                "z": float(sign["frame2"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame2"]["left_knee"]["x"]), 
                "y": float(sign["frame2"]["left_knee"]["y"]), 
                "z": float(sign["frame2"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame2"]["right_knee"]["x"]), 
                "y": float(sign["frame2"]["right_knee"]["y"]), 
                "z": float(sign["frame2"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame2"]["left_ankle"]["x"]), 
                "y": float(sign["frame2"]["left_ankle"]["y"]), 
                "z": float(sign["frame2"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame2"]["right_ankle"]["x"]), 
                "y": float(sign["frame2"]["right_ankle"]["y"]), 
                "z": float(sign["frame2"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame2"]["left_heel"]["x"]), 
                "y": float(sign["frame2"]["left_heel"]["y"]), 
                "z": float(sign["frame2"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame2"]["right_heel"]["x"]), 
                "y": float(sign["frame2"]["right_heel"]["y"]), 
                "z": float(sign["frame2"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame2"]["left_foot_index"]["x"]), 
                "y": float(sign["frame2"]["left_foot_index"]["y"]), 
                "z": float(sign["frame2"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame2"]["right_foot_index"]["x"]), 
                "y": float(sign["frame2"]["right_foot_index"]["y"]), 
                "z": float(sign["frame2"]["right_foot_index"]["z"])
            },
        },
                "frame3": {
            "nose": {
                "x": float(sign["frame3"]["nose"]["x"]), 
                "y": float(sign["frame3"]["nose"]["y"]), 
                "z": float(sign["frame3"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame3"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame3"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame3"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame3"]["left_eye"]["x"]), 
                "y": float(sign["frame3"]["left_eye"]["y"]), 
                "z": float(sign["frame3"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame3"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame3"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame3"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame3"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame3"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame3"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame3"]["right_eye"]["x"]), 
                "y": float(sign["frame3"]["right_eye"]["y"]), 
                "z": float(sign["frame3"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame3"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame3"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame3"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame3"]["left_ear"]["x"]), 
                "y": float(sign["frame3"]["left_ear"]["y"]), 
                "z": float(sign["frame3"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame3"]["right_ear"]["x"]), 
                "y": float(sign["frame3"]["right_ear"]["y"]), 
                "z": float(sign["frame3"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame3"]["mouth_left"]["x"]), 
                "y": float(sign["frame3"]["mouth_left"]["y"]), 
                "z": float(sign["frame3"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame3"]["mouth_right"]["x"]), 
                "y": float(sign["frame3"]["mouth_right"]["y"]), 
                "z": float(sign["frame3"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame3"]["left_shoulder"]["x"]), 
                "y": float(sign["frame3"]["left_shoulder"]["y"]), 
                "z": float(sign["frame3"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame3"]["right_shoulder"]["x"]), 
                "y": float(sign["frame3"]["right_shoulder"]["y"]), 
                "z": float(sign["frame3"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame3"]["left_elbow"]["x"]), 
                "y": float(sign["frame3"]["left_elbow"]["y"]), 
                "z": float(sign["frame3"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame3"]["right_elbow"]["x"]), 
                "y": float(sign["frame3"]["right_elbow"]["y"]), 
                "z": float(sign["frame3"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame3"]["left_wrist"]["x"]), 
                "y": float(sign["frame3"]["left_wrist"]["y"]), 
                "z": float(sign["frame3"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame3"]["right_wrist"]["x"]), 
                "y": float(sign["frame3"]["right_wrist"]["y"]), 
                "z": float(sign["frame3"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame3"]["left_pinky"]["x"]), 
                "y": float(sign["frame3"]["left_pinky"]["y"]), 
                "z": float(sign["frame3"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame3"]["right_pinky"]["x"]), 
                "y": float(sign["frame3"]["right_pinky"]["y"]), 
                "z": float(sign["frame3"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame3"]["left_index"]["x"]), 
                "y": float(sign["frame3"]["left_index"]["y"]), 
                "z": float(sign["frame3"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame3"]["right_index"]["x"]), 
                "y": float(sign["frame3"]["right_index"]["y"]), 
                "z": float(sign["frame3"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame3"]["left_thumb"]["x"]), 
                "y": float(sign["frame3"]["left_thumb"]["y"]), 
                "z": float(sign["frame3"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame3"]["right_thumb"]["x"]), 
                "y": float(sign["frame3"]["right_thumb"]["y"]), 
                "z": float(sign["frame3"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame3"]["left_hip"]["x"]), 
                "y": float(sign["frame3"]["left_hip"]["y"]), 
                "z": float(sign["frame3"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame3"]["right_hip"]["x"]), 
                "y": float(sign["frame3"]["right_hip"]["y"]), 
                "z": float(sign["frame3"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame3"]["left_knee"]["x"]), 
                "y": float(sign["frame3"]["left_knee"]["y"]), 
                "z": float(sign["frame3"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame3"]["right_knee"]["x"]), 
                "y": float(sign["frame3"]["right_knee"]["y"]), 
                "z": float(sign["frame3"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame3"]["left_ankle"]["x"]), 
                "y": float(sign["frame3"]["left_ankle"]["y"]), 
                "z": float(sign["frame3"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame3"]["right_ankle"]["x"]), 
                "y": float(sign["frame3"]["right_ankle"]["y"]), 
                "z": float(sign["frame3"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame3"]["left_heel"]["x"]), 
                "y": float(sign["frame3"]["left_heel"]["y"]), 
                "z": float(sign["frame3"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame3"]["right_heel"]["x"]), 
                "y": float(sign["frame3"]["right_heel"]["y"]), 
                "z": float(sign["frame3"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame3"]["left_foot_index"]["x"]), 
                "y": float(sign["frame3"]["left_foot_index"]["y"]), 
                "z": float(sign["frame3"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame3"]["right_foot_index"]["x"]), 
                "y": float(sign["frame3"]["right_foot_index"]["y"]), 
                "z": float(sign["frame3"]["right_foot_index"]["z"])
            },
        },
                "frame4": {
            "nose": {
                "x": float(sign["frame4"]["nose"]["x"]), 
                "y": float(sign["frame4"]["nose"]["y"]), 
                "z": float(sign["frame4"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame4"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame4"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame4"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame4"]["left_eye"]["x"]), 
                "y": float(sign["frame4"]["left_eye"]["y"]), 
                "z": float(sign["frame4"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame4"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame4"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame4"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame4"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame4"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame4"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame4"]["right_eye"]["x"]), 
                "y": float(sign["frame4"]["right_eye"]["y"]), 
                "z": float(sign["frame4"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame4"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame4"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame4"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame4"]["left_ear"]["x"]), 
                "y": float(sign["frame4"]["left_ear"]["y"]), 
                "z": float(sign["frame4"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame4"]["right_ear"]["x"]), 
                "y": float(sign["frame4"]["right_ear"]["y"]), 
                "z": float(sign["frame4"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame4"]["mouth_left"]["x"]), 
                "y": float(sign["frame4"]["mouth_left"]["y"]), 
                "z": float(sign["frame4"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame4"]["mouth_right"]["x"]), 
                "y": float(sign["frame4"]["mouth_right"]["y"]), 
                "z": float(sign["frame4"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame4"]["left_shoulder"]["x"]), 
                "y": float(sign["frame4"]["left_shoulder"]["y"]), 
                "z": float(sign["frame4"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame4"]["right_shoulder"]["x"]), 
                "y": float(sign["frame4"]["right_shoulder"]["y"]), 
                "z": float(sign["frame4"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame4"]["left_elbow"]["x"]), 
                "y": float(sign["frame4"]["left_elbow"]["y"]), 
                "z": float(sign["frame4"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame4"]["right_elbow"]["x"]), 
                "y": float(sign["frame4"]["right_elbow"]["y"]), 
                "z": float(sign["frame4"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame4"]["left_wrist"]["x"]), 
                "y": float(sign["frame4"]["left_wrist"]["y"]), 
                "z": float(sign["frame4"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame4"]["right_wrist"]["x"]), 
                "y": float(sign["frame4"]["right_wrist"]["y"]), 
                "z": float(sign["frame4"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame4"]["left_pinky"]["x"]), 
                "y": float(sign["frame4"]["left_pinky"]["y"]), 
                "z": float(sign["frame4"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame4"]["right_pinky"]["x"]), 
                "y": float(sign["frame4"]["right_pinky"]["y"]), 
                "z": float(sign["frame4"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame4"]["left_index"]["x"]), 
                "y": float(sign["frame4"]["left_index"]["y"]), 
                "z": float(sign["frame4"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame4"]["right_index"]["x"]), 
                "y": float(sign["frame4"]["right_index"]["y"]), 
                "z": float(sign["frame4"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame4"]["left_thumb"]["x"]), 
                "y": float(sign["frame4"]["left_thumb"]["y"]), 
                "z": float(sign["frame4"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame4"]["right_thumb"]["x"]), 
                "y": float(sign["frame4"]["right_thumb"]["y"]), 
                "z": float(sign["frame4"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame4"]["left_hip"]["x"]), 
                "y": float(sign["frame4"]["left_hip"]["y"]), 
                "z": float(sign["frame4"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame4"]["right_hip"]["x"]), 
                "y": float(sign["frame4"]["right_hip"]["y"]), 
                "z": float(sign["frame4"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame4"]["left_knee"]["x"]), 
                "y": float(sign["frame4"]["left_knee"]["y"]), 
                "z": float(sign["frame4"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame4"]["right_knee"]["x"]), 
                "y": float(sign["frame4"]["right_knee"]["y"]), 
                "z": float(sign["frame4"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame4"]["left_ankle"]["x"]), 
                "y": float(sign["frame4"]["left_ankle"]["y"]), 
                "z": float(sign["frame4"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame4"]["right_ankle"]["x"]), 
                "y": float(sign["frame4"]["right_ankle"]["y"]), 
                "z": float(sign["frame4"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame4"]["left_heel"]["x"]), 
                "y": float(sign["frame4"]["left_heel"]["y"]), 
                "z": float(sign["frame4"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame4"]["right_heel"]["x"]), 
                "y": float(sign["frame4"]["right_heel"]["y"]), 
                "z": float(sign["frame4"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame4"]["left_foot_index"]["x"]), 
                "y": float(sign["frame4"]["left_foot_index"]["y"]), 
                "z": float(sign["frame4"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame4"]["right_foot_index"]["x"]), 
                "y": float(sign["frame4"]["right_foot_index"]["y"]), 
                "z": float(sign["frame4"]["right_foot_index"]["z"])
            },
        },
                "frame5": {
            "nose": {
                "x": float(sign["frame5"]["nose"]["x"]), 
                "y": float(sign["frame5"]["nose"]["y"]), 
                "z": float(sign["frame5"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame5"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame5"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame5"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame5"]["left_eye"]["x"]), 
                "y": float(sign["frame5"]["left_eye"]["y"]), 
                "z": float(sign["frame5"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame5"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame5"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame5"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame5"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame5"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame5"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame5"]["right_eye"]["x"]), 
                "y": float(sign["frame5"]["right_eye"]["y"]), 
                "z": float(sign["frame5"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame5"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame5"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame5"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame5"]["left_ear"]["x"]), 
                "y": float(sign["frame5"]["left_ear"]["y"]), 
                "z": float(sign["frame5"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame5"]["right_ear"]["x"]), 
                "y": float(sign["frame5"]["right_ear"]["y"]), 
                "z": float(sign["frame5"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame5"]["mouth_left"]["x"]), 
                "y": float(sign["frame5"]["mouth_left"]["y"]), 
                "z": float(sign["frame5"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame5"]["mouth_right"]["x"]), 
                "y": float(sign["frame5"]["mouth_right"]["y"]), 
                "z": float(sign["frame5"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame5"]["left_shoulder"]["x"]), 
                "y": float(sign["frame5"]["left_shoulder"]["y"]), 
                "z": float(sign["frame5"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame5"]["right_shoulder"]["x"]), 
                "y": float(sign["frame5"]["right_shoulder"]["y"]), 
                "z": float(sign["frame5"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame5"]["left_elbow"]["x"]), 
                "y": float(sign["frame5"]["left_elbow"]["y"]), 
                "z": float(sign["frame5"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame5"]["right_elbow"]["x"]), 
                "y": float(sign["frame5"]["right_elbow"]["y"]), 
                "z": float(sign["frame5"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame5"]["left_wrist"]["x"]), 
                "y": float(sign["frame5"]["left_wrist"]["y"]), 
                "z": float(sign["frame5"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame5"]["right_wrist"]["x"]), 
                "y": float(sign["frame5"]["right_wrist"]["y"]), 
                "z": float(sign["frame5"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame5"]["left_pinky"]["x"]), 
                "y": float(sign["frame5"]["left_pinky"]["y"]), 
                "z": float(sign["frame5"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame5"]["right_pinky"]["x"]), 
                "y": float(sign["frame5"]["right_pinky"]["y"]), 
                "z": float(sign["frame5"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame5"]["left_index"]["x"]), 
                "y": float(sign["frame5"]["left_index"]["y"]), 
                "z": float(sign["frame5"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame5"]["right_index"]["x"]), 
                "y": float(sign["frame5"]["right_index"]["y"]), 
                "z": float(sign["frame5"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame5"]["left_thumb"]["x"]), 
                "y": float(sign["frame5"]["left_thumb"]["y"]), 
                "z": float(sign["frame5"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame5"]["right_thumb"]["x"]), 
                "y": float(sign["frame5"]["right_thumb"]["y"]), 
                "z": float(sign["frame5"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame5"]["left_hip"]["x"]), 
                "y": float(sign["frame5"]["left_hip"]["y"]), 
                "z": float(sign["frame5"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame5"]["right_hip"]["x"]), 
                "y": float(sign["frame5"]["right_hip"]["y"]), 
                "z": float(sign["frame5"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame5"]["left_knee"]["x"]), 
                "y": float(sign["frame5"]["left_knee"]["y"]), 
                "z": float(sign["frame5"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame5"]["right_knee"]["x"]), 
                "y": float(sign["frame5"]["right_knee"]["y"]), 
                "z": float(sign["frame5"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame5"]["left_ankle"]["x"]), 
                "y": float(sign["frame5"]["left_ankle"]["y"]), 
                "z": float(sign["frame5"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame5"]["right_ankle"]["x"]), 
                "y": float(sign["frame5"]["right_ankle"]["y"]), 
                "z": float(sign["frame5"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame5"]["left_heel"]["x"]), 
                "y": float(sign["frame5"]["left_heel"]["y"]), 
                "z": float(sign["frame5"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame5"]["right_heel"]["x"]), 
                "y": float(sign["frame5"]["right_heel"]["y"]), 
                "z": float(sign["frame5"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame5"]["left_foot_index"]["x"]), 
                "y": float(sign["frame5"]["left_foot_index"]["y"]), 
                "z": float(sign["frame5"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame5"]["right_foot_index"]["x"]), 
                "y": float(sign["frame5"]["right_foot_index"]["y"]), 
                "z": float(sign["frame5"]["right_foot_index"]["z"])
            },
        },
                "frame6": {
            "nose": {
                "x": float(sign["frame6"]["nose"]["x"]), 
                "y": float(sign["frame6"]["nose"]["y"]), 
                "z": float(sign["frame6"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame6"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame6"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame6"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame6"]["left_eye"]["x"]), 
                "y": float(sign["frame6"]["left_eye"]["y"]), 
                "z": float(sign["frame6"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame6"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame6"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame6"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame6"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame6"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame6"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame6"]["right_eye"]["x"]), 
                "y": float(sign["frame6"]["right_eye"]["y"]), 
                "z": float(sign["frame6"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame6"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame6"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame6"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame6"]["left_ear"]["x"]), 
                "y": float(sign["frame6"]["left_ear"]["y"]), 
                "z": float(sign["frame6"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame6"]["right_ear"]["x"]), 
                "y": float(sign["frame6"]["right_ear"]["y"]), 
                "z": float(sign["frame6"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame6"]["mouth_left"]["x"]), 
                "y": float(sign["frame6"]["mouth_left"]["y"]), 
                "z": float(sign["frame6"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame6"]["mouth_right"]["x"]), 
                "y": float(sign["frame6"]["mouth_right"]["y"]), 
                "z": float(sign["frame6"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame6"]["left_shoulder"]["x"]), 
                "y": float(sign["frame6"]["left_shoulder"]["y"]), 
                "z": float(sign["frame6"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame6"]["right_shoulder"]["x"]), 
                "y": float(sign["frame6"]["right_shoulder"]["y"]), 
                "z": float(sign["frame6"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame6"]["left_elbow"]["x"]), 
                "y": float(sign["frame6"]["left_elbow"]["y"]), 
                "z": float(sign["frame6"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame6"]["right_elbow"]["x"]), 
                "y": float(sign["frame6"]["right_elbow"]["y"]), 
                "z": float(sign["frame6"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame6"]["left_wrist"]["x"]), 
                "y": float(sign["frame6"]["left_wrist"]["y"]), 
                "z": float(sign["frame6"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame6"]["right_wrist"]["x"]), 
                "y": float(sign["frame6"]["right_wrist"]["y"]), 
                "z": float(sign["frame6"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame6"]["left_pinky"]["x"]), 
                "y": float(sign["frame6"]["left_pinky"]["y"]), 
                "z": float(sign["frame6"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame6"]["right_pinky"]["x"]), 
                "y": float(sign["frame6"]["right_pinky"]["y"]), 
                "z": float(sign["frame6"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame6"]["left_index"]["x"]), 
                "y": float(sign["frame6"]["left_index"]["y"]), 
                "z": float(sign["frame6"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame6"]["right_index"]["x"]), 
                "y": float(sign["frame6"]["right_index"]["y"]), 
                "z": float(sign["frame6"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame6"]["left_thumb"]["x"]), 
                "y": float(sign["frame6"]["left_thumb"]["y"]), 
                "z": float(sign["frame6"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame6"]["right_thumb"]["x"]), 
                "y": float(sign["frame6"]["right_thumb"]["y"]), 
                "z": float(sign["frame6"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame6"]["left_hip"]["x"]), 
                "y": float(sign["frame6"]["left_hip"]["y"]), 
                "z": float(sign["frame6"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame6"]["right_hip"]["x"]), 
                "y": float(sign["frame6"]["right_hip"]["y"]), 
                "z": float(sign["frame6"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame6"]["left_knee"]["x"]), 
                "y": float(sign["frame6"]["left_knee"]["y"]), 
                "z": float(sign["frame6"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame6"]["right_knee"]["x"]), 
                "y": float(sign["frame6"]["right_knee"]["y"]), 
                "z": float(sign["frame6"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame6"]["left_ankle"]["x"]), 
                "y": float(sign["frame6"]["left_ankle"]["y"]), 
                "z": float(sign["frame6"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame6"]["right_ankle"]["x"]), 
                "y": float(sign["frame6"]["right_ankle"]["y"]), 
                "z": float(sign["frame6"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame6"]["left_heel"]["x"]), 
                "y": float(sign["frame6"]["left_heel"]["y"]), 
                "z": float(sign["frame6"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame6"]["right_heel"]["x"]), 
                "y": float(sign["frame6"]["right_heel"]["y"]), 
                "z": float(sign["frame6"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame6"]["left_foot_index"]["x"]), 
                "y": float(sign["frame6"]["left_foot_index"]["y"]), 
                "z": float(sign["frame6"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame6"]["right_foot_index"]["x"]), 
                "y": float(sign["frame6"]["right_foot_index"]["y"]), 
                "z": float(sign["frame6"]["right_foot_index"]["z"])
            },
        },
                "frame7": {
            "nose": {
                "x": float(sign["frame7"]["nose"]["x"]), 
                "y": float(sign["frame7"]["nose"]["y"]), 
                "z": float(sign["frame7"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame7"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame7"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame7"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame7"]["left_eye"]["x"]), 
                "y": float(sign["frame7"]["left_eye"]["y"]), 
                "z": float(sign["frame7"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame7"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame7"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame7"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame7"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame7"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame7"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame7"]["right_eye"]["x"]), 
                "y": float(sign["frame7"]["right_eye"]["y"]), 
                "z": float(sign["frame7"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame7"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame7"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame7"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame7"]["left_ear"]["x"]), 
                "y": float(sign["frame7"]["left_ear"]["y"]), 
                "z": float(sign["frame7"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame7"]["right_ear"]["x"]), 
                "y": float(sign["frame7"]["right_ear"]["y"]), 
                "z": float(sign["frame7"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame7"]["mouth_left"]["x"]), 
                "y": float(sign["frame7"]["mouth_left"]["y"]), 
                "z": float(sign["frame7"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame7"]["mouth_right"]["x"]), 
                "y": float(sign["frame7"]["mouth_right"]["y"]), 
                "z": float(sign["frame7"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame7"]["left_shoulder"]["x"]), 
                "y": float(sign["frame7"]["left_shoulder"]["y"]), 
                "z": float(sign["frame7"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame7"]["right_shoulder"]["x"]), 
                "y": float(sign["frame7"]["right_shoulder"]["y"]), 
                "z": float(sign["frame7"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame7"]["left_elbow"]["x"]), 
                "y": float(sign["frame7"]["left_elbow"]["y"]), 
                "z": float(sign["frame7"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame7"]["right_elbow"]["x"]), 
                "y": float(sign["frame7"]["right_elbow"]["y"]), 
                "z": float(sign["frame7"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame7"]["left_wrist"]["x"]), 
                "y": float(sign["frame7"]["left_wrist"]["y"]), 
                "z": float(sign["frame7"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame7"]["right_wrist"]["x"]), 
                "y": float(sign["frame7"]["right_wrist"]["y"]), 
                "z": float(sign["frame7"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame7"]["left_pinky"]["x"]), 
                "y": float(sign["frame7"]["left_pinky"]["y"]), 
                "z": float(sign["frame7"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame7"]["right_pinky"]["x"]), 
                "y": float(sign["frame7"]["right_pinky"]["y"]), 
                "z": float(sign["frame7"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame7"]["left_index"]["x"]), 
                "y": float(sign["frame7"]["left_index"]["y"]), 
                "z": float(sign["frame7"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame7"]["right_index"]["x"]), 
                "y": float(sign["frame7"]["right_index"]["y"]), 
                "z": float(sign["frame7"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame7"]["left_thumb"]["x"]), 
                "y": float(sign["frame7"]["left_thumb"]["y"]), 
                "z": float(sign["frame7"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame7"]["right_thumb"]["x"]), 
                "y": float(sign["frame7"]["right_thumb"]["y"]), 
                "z": float(sign["frame7"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame7"]["left_hip"]["x"]), 
                "y": float(sign["frame7"]["left_hip"]["y"]), 
                "z": float(sign["frame7"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame7"]["right_hip"]["x"]), 
                "y": float(sign["frame7"]["right_hip"]["y"]), 
                "z": float(sign["frame7"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame7"]["left_knee"]["x"]), 
                "y": float(sign["frame7"]["left_knee"]["y"]), 
                "z": float(sign["frame7"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame7"]["right_knee"]["x"]), 
                "y": float(sign["frame7"]["right_knee"]["y"]), 
                "z": float(sign["frame7"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame7"]["left_ankle"]["x"]), 
                "y": float(sign["frame7"]["left_ankle"]["y"]), 
                "z": float(sign["frame7"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame7"]["right_ankle"]["x"]), 
                "y": float(sign["frame7"]["right_ankle"]["y"]), 
                "z": float(sign["frame7"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame7"]["left_heel"]["x"]), 
                "y": float(sign["frame7"]["left_heel"]["y"]), 
                "z": float(sign["frame7"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame7"]["right_heel"]["x"]), 
                "y": float(sign["frame7"]["right_heel"]["y"]), 
                "z": float(sign["frame7"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame7"]["left_foot_index"]["x"]), 
                "y": float(sign["frame7"]["left_foot_index"]["y"]), 
                "z": float(sign["frame7"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame7"]["right_foot_index"]["x"]), 
                "y": float(sign["frame7"]["right_foot_index"]["y"]), 
                "z": float(sign["frame7"]["right_foot_index"]["z"])
            },
        },
                "frame8": {
            "nose": {
                "x": float(sign["frame8"]["nose"]["x"]), 
                "y": float(sign["frame8"]["nose"]["y"]), 
                "z": float(sign["frame8"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame8"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame8"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame8"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame8"]["left_eye"]["x"]), 
                "y": float(sign["frame8"]["left_eye"]["y"]), 
                "z": float(sign["frame8"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame8"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame8"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame8"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame8"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame8"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame8"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame8"]["right_eye"]["x"]), 
                "y": float(sign["frame8"]["right_eye"]["y"]), 
                "z": float(sign["frame8"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame8"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame8"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame8"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame8"]["left_ear"]["x"]), 
                "y": float(sign["frame8"]["left_ear"]["y"]), 
                "z": float(sign["frame8"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame8"]["right_ear"]["x"]), 
                "y": float(sign["frame8"]["right_ear"]["y"]), 
                "z": float(sign["frame8"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame8"]["mouth_left"]["x"]), 
                "y": float(sign["frame8"]["mouth_left"]["y"]), 
                "z": float(sign["frame8"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame8"]["mouth_right"]["x"]), 
                "y": float(sign["frame8"]["mouth_right"]["y"]), 
                "z": float(sign["frame8"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame8"]["left_shoulder"]["x"]), 
                "y": float(sign["frame8"]["left_shoulder"]["y"]), 
                "z": float(sign["frame8"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame8"]["right_shoulder"]["x"]), 
                "y": float(sign["frame8"]["right_shoulder"]["y"]), 
                "z": float(sign["frame8"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame8"]["left_elbow"]["x"]), 
                "y": float(sign["frame8"]["left_elbow"]["y"]), 
                "z": float(sign["frame8"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame8"]["right_elbow"]["x"]), 
                "y": float(sign["frame8"]["right_elbow"]["y"]), 
                "z": float(sign["frame8"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame8"]["left_wrist"]["x"]), 
                "y": float(sign["frame8"]["left_wrist"]["y"]), 
                "z": float(sign["frame8"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame8"]["right_wrist"]["x"]), 
                "y": float(sign["frame8"]["right_wrist"]["y"]), 
                "z": float(sign["frame8"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame8"]["left_pinky"]["x"]), 
                "y": float(sign["frame8"]["left_pinky"]["y"]), 
                "z": float(sign["frame8"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame8"]["right_pinky"]["x"]), 
                "y": float(sign["frame8"]["right_pinky"]["y"]), 
                "z": float(sign["frame8"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame8"]["left_index"]["x"]), 
                "y": float(sign["frame8"]["left_index"]["y"]), 
                "z": float(sign["frame8"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame8"]["right_index"]["x"]), 
                "y": float(sign["frame8"]["right_index"]["y"]), 
                "z": float(sign["frame8"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame8"]["left_thumb"]["x"]), 
                "y": float(sign["frame8"]["left_thumb"]["y"]), 
                "z": float(sign["frame8"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame8"]["right_thumb"]["x"]), 
                "y": float(sign["frame8"]["right_thumb"]["y"]), 
                "z": float(sign["frame8"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame8"]["left_hip"]["x"]), 
                "y": float(sign["frame8"]["left_hip"]["y"]), 
                "z": float(sign["frame8"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame8"]["right_hip"]["x"]), 
                "y": float(sign["frame8"]["right_hip"]["y"]), 
                "z": float(sign["frame8"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame8"]["left_knee"]["x"]), 
                "y": float(sign["frame8"]["left_knee"]["y"]), 
                "z": float(sign["frame8"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame8"]["right_knee"]["x"]), 
                "y": float(sign["frame8"]["right_knee"]["y"]), 
                "z": float(sign["frame8"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame8"]["left_ankle"]["x"]), 
                "y": float(sign["frame8"]["left_ankle"]["y"]), 
                "z": float(sign["frame8"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame8"]["right_ankle"]["x"]), 
                "y": float(sign["frame8"]["right_ankle"]["y"]), 
                "z": float(sign["frame8"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame8"]["left_heel"]["x"]), 
                "y": float(sign["frame8"]["left_heel"]["y"]), 
                "z": float(sign["frame8"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame8"]["right_heel"]["x"]), 
                "y": float(sign["frame8"]["right_heel"]["y"]), 
                "z": float(sign["frame8"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame8"]["left_foot_index"]["x"]), 
                "y": float(sign["frame8"]["left_foot_index"]["y"]), 
                "z": float(sign["frame8"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame8"]["right_foot_index"]["x"]), 
                "y": float(sign["frame8"]["right_foot_index"]["y"]), 
                "z": float(sign["frame8"]["right_foot_index"]["z"])
            },
        },
                "frame9": {
            "nose": {
                "x": float(sign["frame9"]["nose"]["x"]), 
                "y": float(sign["frame9"]["nose"]["y"]), 
                "z": float(sign["frame9"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame9"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame9"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame9"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame9"]["left_eye"]["x"]), 
                "y": float(sign["frame9"]["left_eye"]["y"]), 
                "z": float(sign["frame9"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame9"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame9"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame9"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame9"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame9"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame9"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame9"]["right_eye"]["x"]), 
                "y": float(sign["frame9"]["right_eye"]["y"]), 
                "z": float(sign["frame9"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame9"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame9"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame9"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame9"]["left_ear"]["x"]), 
                "y": float(sign["frame9"]["left_ear"]["y"]), 
                "z": float(sign["frame9"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame9"]["right_ear"]["x"]), 
                "y": float(sign["frame9"]["right_ear"]["y"]), 
                "z": float(sign["frame9"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame9"]["mouth_left"]["x"]), 
                "y": float(sign["frame9"]["mouth_left"]["y"]), 
                "z": float(sign["frame9"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame9"]["mouth_right"]["x"]), 
                "y": float(sign["frame9"]["mouth_right"]["y"]), 
                "z": float(sign["frame9"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame9"]["left_shoulder"]["x"]), 
                "y": float(sign["frame9"]["left_shoulder"]["y"]), 
                "z": float(sign["frame9"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame9"]["right_shoulder"]["x"]), 
                "y": float(sign["frame9"]["right_shoulder"]["y"]), 
                "z": float(sign["frame9"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame9"]["left_elbow"]["x"]), 
                "y": float(sign["frame9"]["left_elbow"]["y"]), 
                "z": float(sign["frame9"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame9"]["right_elbow"]["x"]), 
                "y": float(sign["frame9"]["right_elbow"]["y"]), 
                "z": float(sign["frame9"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame9"]["left_wrist"]["x"]), 
                "y": float(sign["frame9"]["left_wrist"]["y"]), 
                "z": float(sign["frame9"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame9"]["right_wrist"]["x"]), 
                "y": float(sign["frame9"]["right_wrist"]["y"]), 
                "z": float(sign["frame9"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame9"]["left_pinky"]["x"]), 
                "y": float(sign["frame9"]["left_pinky"]["y"]), 
                "z": float(sign["frame9"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame9"]["right_pinky"]["x"]), 
                "y": float(sign["frame9"]["right_pinky"]["y"]), 
                "z": float(sign["frame9"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame9"]["left_index"]["x"]), 
                "y": float(sign["frame9"]["left_index"]["y"]), 
                "z": float(sign["frame9"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame9"]["right_index"]["x"]), 
                "y": float(sign["frame9"]["right_index"]["y"]), 
                "z": float(sign["frame9"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame9"]["left_thumb"]["x"]), 
                "y": float(sign["frame9"]["left_thumb"]["y"]), 
                "z": float(sign["frame9"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame9"]["right_thumb"]["x"]), 
                "y": float(sign["frame9"]["right_thumb"]["y"]), 
                "z": float(sign["frame9"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame9"]["left_hip"]["x"]), 
                "y": float(sign["frame9"]["left_hip"]["y"]), 
                "z": float(sign["frame9"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame9"]["right_hip"]["x"]), 
                "y": float(sign["frame9"]["right_hip"]["y"]), 
                "z": float(sign["frame9"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame9"]["left_knee"]["x"]), 
                "y": float(sign["frame9"]["left_knee"]["y"]), 
                "z": float(sign["frame9"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame9"]["right_knee"]["x"]), 
                "y": float(sign["frame9"]["right_knee"]["y"]), 
                "z": float(sign["frame9"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame9"]["left_ankle"]["x"]), 
                "y": float(sign["frame9"]["left_ankle"]["y"]), 
                "z": float(sign["frame9"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame9"]["right_ankle"]["x"]), 
                "y": float(sign["frame9"]["right_ankle"]["y"]), 
                "z": float(sign["frame9"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame9"]["left_heel"]["x"]), 
                "y": float(sign["frame9"]["left_heel"]["y"]), 
                "z": float(sign["frame9"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame9"]["right_heel"]["x"]), 
                "y": float(sign["frame9"]["right_heel"]["y"]), 
                "z": float(sign["frame9"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame9"]["left_foot_index"]["x"]), 
                "y": float(sign["frame9"]["left_foot_index"]["y"]), 
                "z": float(sign["frame9"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame9"]["right_foot_index"]["x"]), 
                "y": float(sign["frame9"]["right_foot_index"]["y"]), 
                "z": float(sign["frame9"]["right_foot_index"]["z"])
            },
        },
                "frame10": {
            "nose": {
                "x": float(sign["frame10"]["nose"]["x"]), 
                "y": float(sign["frame10"]["nose"]["y"]), 
                "z": float(sign["frame10"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame10"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame10"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame10"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame10"]["left_eye"]["x"]), 
                "y": float(sign["frame10"]["left_eye"]["y"]), 
                "z": float(sign["frame10"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame10"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame10"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame10"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame10"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame10"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame10"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame10"]["right_eye"]["x"]), 
                "y": float(sign["frame10"]["right_eye"]["y"]), 
                "z": float(sign["frame10"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame10"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame10"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame10"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame10"]["left_ear"]["x"]), 
                "y": float(sign["frame10"]["left_ear"]["y"]), 
                "z": float(sign["frame10"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame10"]["right_ear"]["x"]), 
                "y": float(sign["frame10"]["right_ear"]["y"]), 
                "z": float(sign["frame10"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame10"]["mouth_left"]["x"]), 
                "y": float(sign["frame10"]["mouth_left"]["y"]), 
                "z": float(sign["frame10"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame10"]["mouth_right"]["x"]), 
                "y": float(sign["frame10"]["mouth_right"]["y"]), 
                "z": float(sign["frame10"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame10"]["left_shoulder"]["x"]), 
                "y": float(sign["frame10"]["left_shoulder"]["y"]), 
                "z": float(sign["frame10"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame10"]["right_shoulder"]["x"]), 
                "y": float(sign["frame10"]["right_shoulder"]["y"]), 
                "z": float(sign["frame10"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame10"]["left_elbow"]["x"]), 
                "y": float(sign["frame10"]["left_elbow"]["y"]), 
                "z": float(sign["frame10"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame10"]["right_elbow"]["x"]), 
                "y": float(sign["frame10"]["right_elbow"]["y"]), 
                "z": float(sign["frame10"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame10"]["left_wrist"]["x"]), 
                "y": float(sign["frame10"]["left_wrist"]["y"]), 
                "z": float(sign["frame10"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame10"]["right_wrist"]["x"]), 
                "y": float(sign["frame10"]["right_wrist"]["y"]), 
                "z": float(sign["frame10"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame10"]["left_pinky"]["x"]), 
                "y": float(sign["frame10"]["left_pinky"]["y"]), 
                "z": float(sign["frame10"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame10"]["right_pinky"]["x"]), 
                "y": float(sign["frame10"]["right_pinky"]["y"]), 
                "z": float(sign["frame10"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame10"]["left_index"]["x"]), 
                "y": float(sign["frame10"]["left_index"]["y"]), 
                "z": float(sign["frame10"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame10"]["right_index"]["x"]), 
                "y": float(sign["frame10"]["right_index"]["y"]), 
                "z": float(sign["frame10"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame10"]["left_thumb"]["x"]), 
                "y": float(sign["frame10"]["left_thumb"]["y"]), 
                "z": float(sign["frame10"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame10"]["right_thumb"]["x"]), 
                "y": float(sign["frame10"]["right_thumb"]["y"]), 
                "z": float(sign["frame10"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame10"]["left_hip"]["x"]), 
                "y": float(sign["frame10"]["left_hip"]["y"]), 
                "z": float(sign["frame10"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame10"]["right_hip"]["x"]), 
                "y": float(sign["frame10"]["right_hip"]["y"]), 
                "z": float(sign["frame10"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame10"]["left_knee"]["x"]), 
                "y": float(sign["frame10"]["left_knee"]["y"]), 
                "z": float(sign["frame10"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame10"]["right_knee"]["x"]), 
                "y": float(sign["frame10"]["right_knee"]["y"]), 
                "z": float(sign["frame10"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame10"]["left_ankle"]["x"]), 
                "y": float(sign["frame10"]["left_ankle"]["y"]), 
                "z": float(sign["frame10"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame10"]["right_ankle"]["x"]), 
                "y": float(sign["frame10"]["right_ankle"]["y"]), 
                "z": float(sign["frame10"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame10"]["left_heel"]["x"]), 
                "y": float(sign["frame10"]["left_heel"]["y"]), 
                "z": float(sign["frame10"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame10"]["right_heel"]["x"]), 
                "y": float(sign["frame10"]["right_heel"]["y"]), 
                "z": float(sign["frame10"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame10"]["left_foot_index"]["x"]), 
                "y": float(sign["frame10"]["left_foot_index"]["y"]), 
                "z": float(sign["frame10"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame10"]["right_foot_index"]["x"]), 
                "y": float(sign["frame10"]["right_foot_index"]["y"]), 
                "z": float(sign["frame10"]["right_foot_index"]["z"])
            },
        },
                "frame11": {
            "nose": {
                "x": float(sign["frame11"]["nose"]["x"]), 
                "y": float(sign["frame11"]["nose"]["y"]), 
                "z": float(sign["frame11"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame11"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame11"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame11"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame11"]["left_eye"]["x"]), 
                "y": float(sign["frame11"]["left_eye"]["y"]), 
                "z": float(sign["frame11"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame11"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame11"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame11"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame11"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame11"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame11"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame11"]["right_eye"]["x"]), 
                "y": float(sign["frame11"]["right_eye"]["y"]), 
                "z": float(sign["frame11"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame11"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame11"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame11"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame11"]["left_ear"]["x"]), 
                "y": float(sign["frame11"]["left_ear"]["y"]), 
                "z": float(sign["frame11"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame11"]["right_ear"]["x"]), 
                "y": float(sign["frame11"]["right_ear"]["y"]), 
                "z": float(sign["frame11"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame11"]["mouth_left"]["x"]), 
                "y": float(sign["frame11"]["mouth_left"]["y"]), 
                "z": float(sign["frame11"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame11"]["mouth_right"]["x"]), 
                "y": float(sign["frame11"]["mouth_right"]["y"]), 
                "z": float(sign["frame11"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame11"]["left_shoulder"]["x"]), 
                "y": float(sign["frame11"]["left_shoulder"]["y"]), 
                "z": float(sign["frame11"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame11"]["right_shoulder"]["x"]), 
                "y": float(sign["frame11"]["right_shoulder"]["y"]), 
                "z": float(sign["frame11"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame11"]["left_elbow"]["x"]), 
                "y": float(sign["frame11"]["left_elbow"]["y"]), 
                "z": float(sign["frame11"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame11"]["right_elbow"]["x"]), 
                "y": float(sign["frame11"]["right_elbow"]["y"]), 
                "z": float(sign["frame11"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame11"]["left_wrist"]["x"]), 
                "y": float(sign["frame11"]["left_wrist"]["y"]), 
                "z": float(sign["frame11"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame11"]["right_wrist"]["x"]), 
                "y": float(sign["frame11"]["right_wrist"]["y"]), 
                "z": float(sign["frame11"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame11"]["left_pinky"]["x"]), 
                "y": float(sign["frame11"]["left_pinky"]["y"]), 
                "z": float(sign["frame11"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame11"]["right_pinky"]["x"]), 
                "y": float(sign["frame11"]["right_pinky"]["y"]), 
                "z": float(sign["frame11"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame11"]["left_index"]["x"]), 
                "y": float(sign["frame11"]["left_index"]["y"]), 
                "z": float(sign["frame11"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame11"]["right_index"]["x"]), 
                "y": float(sign["frame11"]["right_index"]["y"]), 
                "z": float(sign["frame11"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame11"]["left_thumb"]["x"]), 
                "y": float(sign["frame11"]["left_thumb"]["y"]), 
                "z": float(sign["frame11"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame11"]["right_thumb"]["x"]), 
                "y": float(sign["frame11"]["right_thumb"]["y"]), 
                "z": float(sign["frame11"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame11"]["left_hip"]["x"]), 
                "y": float(sign["frame11"]["left_hip"]["y"]), 
                "z": float(sign["frame11"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame11"]["right_hip"]["x"]), 
                "y": float(sign["frame11"]["right_hip"]["y"]), 
                "z": float(sign["frame11"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame11"]["left_knee"]["x"]), 
                "y": float(sign["frame11"]["left_knee"]["y"]), 
                "z": float(sign["frame11"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame11"]["right_knee"]["x"]), 
                "y": float(sign["frame11"]["right_knee"]["y"]), 
                "z": float(sign["frame11"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame11"]["left_ankle"]["x"]), 
                "y": float(sign["frame11"]["left_ankle"]["y"]), 
                "z": float(sign["frame11"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame11"]["right_ankle"]["x"]), 
                "y": float(sign["frame11"]["right_ankle"]["y"]), 
                "z": float(sign["frame11"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame11"]["left_heel"]["x"]), 
                "y": float(sign["frame11"]["left_heel"]["y"]), 
                "z": float(sign["frame11"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame11"]["right_heel"]["x"]), 
                "y": float(sign["frame11"]["right_heel"]["y"]), 
                "z": float(sign["frame11"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame11"]["left_foot_index"]["x"]), 
                "y": float(sign["frame11"]["left_foot_index"]["y"]), 
                "z": float(sign["frame11"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame11"]["right_foot_index"]["x"]), 
                "y": float(sign["frame11"]["right_foot_index"]["y"]), 
                "z": float(sign["frame11"]["right_foot_index"]["z"])
            },
        },
                "frame12": {
            "nose": {
                "x": float(sign["frame12"]["nose"]["x"]), 
                "y": float(sign["frame12"]["nose"]["y"]), 
                "z": float(sign["frame12"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame12"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame12"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame12"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame12"]["left_eye"]["x"]), 
                "y": float(sign["frame12"]["left_eye"]["y"]), 
                "z": float(sign["frame12"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame12"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame12"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame12"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame12"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame12"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame12"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame12"]["right_eye"]["x"]), 
                "y": float(sign["frame12"]["right_eye"]["y"]), 
                "z": float(sign["frame12"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame12"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame12"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame12"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame12"]["left_ear"]["x"]), 
                "y": float(sign["frame12"]["left_ear"]["y"]), 
                "z": float(sign["frame12"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame12"]["right_ear"]["x"]), 
                "y": float(sign["frame12"]["right_ear"]["y"]), 
                "z": float(sign["frame12"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame12"]["mouth_left"]["x"]), 
                "y": float(sign["frame12"]["mouth_left"]["y"]), 
                "z": float(sign["frame12"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame12"]["mouth_right"]["x"]), 
                "y": float(sign["frame12"]["mouth_right"]["y"]), 
                "z": float(sign["frame12"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame12"]["left_shoulder"]["x"]), 
                "y": float(sign["frame12"]["left_shoulder"]["y"]), 
                "z": float(sign["frame12"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame12"]["right_shoulder"]["x"]), 
                "y": float(sign["frame12"]["right_shoulder"]["y"]), 
                "z": float(sign["frame12"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame12"]["left_elbow"]["x"]), 
                "y": float(sign["frame12"]["left_elbow"]["y"]), 
                "z": float(sign["frame12"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame12"]["right_elbow"]["x"]), 
                "y": float(sign["frame12"]["right_elbow"]["y"]), 
                "z": float(sign["frame12"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame12"]["left_wrist"]["x"]), 
                "y": float(sign["frame12"]["left_wrist"]["y"]), 
                "z": float(sign["frame12"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame12"]["right_wrist"]["x"]), 
                "y": float(sign["frame12"]["right_wrist"]["y"]), 
                "z": float(sign["frame12"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame12"]["left_pinky"]["x"]), 
                "y": float(sign["frame12"]["left_pinky"]["y"]), 
                "z": float(sign["frame12"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame12"]["right_pinky"]["x"]), 
                "y": float(sign["frame12"]["right_pinky"]["y"]), 
                "z": float(sign["frame12"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame12"]["left_index"]["x"]), 
                "y": float(sign["frame12"]["left_index"]["y"]), 
                "z": float(sign["frame12"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame12"]["right_index"]["x"]), 
                "y": float(sign["frame12"]["right_index"]["y"]), 
                "z": float(sign["frame12"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame12"]["left_thumb"]["x"]), 
                "y": float(sign["frame12"]["left_thumb"]["y"]), 
                "z": float(sign["frame12"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame12"]["right_thumb"]["x"]), 
                "y": float(sign["frame12"]["right_thumb"]["y"]), 
                "z": float(sign["frame12"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame12"]["left_hip"]["x"]), 
                "y": float(sign["frame12"]["left_hip"]["y"]), 
                "z": float(sign["frame12"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame12"]["right_hip"]["x"]), 
                "y": float(sign["frame12"]["right_hip"]["y"]), 
                "z": float(sign["frame12"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame12"]["left_knee"]["x"]), 
                "y": float(sign["frame12"]["left_knee"]["y"]), 
                "z": float(sign["frame12"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame12"]["right_knee"]["x"]), 
                "y": float(sign["frame12"]["right_knee"]["y"]), 
                "z": float(sign["frame12"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame12"]["left_ankle"]["x"]), 
                "y": float(sign["frame12"]["left_ankle"]["y"]), 
                "z": float(sign["frame12"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame12"]["right_ankle"]["x"]), 
                "y": float(sign["frame12"]["right_ankle"]["y"]), 
                "z": float(sign["frame12"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame12"]["left_heel"]["x"]), 
                "y": float(sign["frame12"]["left_heel"]["y"]), 
                "z": float(sign["frame12"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame12"]["right_heel"]["x"]), 
                "y": float(sign["frame12"]["right_heel"]["y"]), 
                "z": float(sign["frame12"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame12"]["left_foot_index"]["x"]), 
                "y": float(sign["frame12"]["left_foot_index"]["y"]), 
                "z": float(sign["frame12"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame12"]["right_foot_index"]["x"]), 
                "y": float(sign["frame12"]["right_foot_index"]["y"]), 
                "z": float(sign["frame12"]["right_foot_index"]["z"])
            },
        },
                "frame13": {
            "nose": {
                "x": float(sign["frame13"]["nose"]["x"]), 
                "y": float(sign["frame13"]["nose"]["y"]), 
                "z": float(sign["frame13"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame13"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame13"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame13"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame13"]["left_eye"]["x"]), 
                "y": float(sign["frame13"]["left_eye"]["y"]), 
                "z": float(sign["frame13"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame13"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame13"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame13"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame13"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame13"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame13"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame13"]["right_eye"]["x"]), 
                "y": float(sign["frame13"]["right_eye"]["y"]), 
                "z": float(sign["frame13"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame13"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame13"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame13"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame13"]["left_ear"]["x"]), 
                "y": float(sign["frame13"]["left_ear"]["y"]), 
                "z": float(sign["frame13"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame13"]["right_ear"]["x"]), 
                "y": float(sign["frame13"]["right_ear"]["y"]), 
                "z": float(sign["frame13"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame13"]["mouth_left"]["x"]), 
                "y": float(sign["frame13"]["mouth_left"]["y"]), 
                "z": float(sign["frame13"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame13"]["mouth_right"]["x"]), 
                "y": float(sign["frame13"]["mouth_right"]["y"]), 
                "z": float(sign["frame13"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame13"]["left_shoulder"]["x"]), 
                "y": float(sign["frame13"]["left_shoulder"]["y"]), 
                "z": float(sign["frame13"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame13"]["right_shoulder"]["x"]), 
                "y": float(sign["frame13"]["right_shoulder"]["y"]), 
                "z": float(sign["frame13"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame13"]["left_elbow"]["x"]), 
                "y": float(sign["frame13"]["left_elbow"]["y"]), 
                "z": float(sign["frame13"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame13"]["right_elbow"]["x"]), 
                "y": float(sign["frame13"]["right_elbow"]["y"]), 
                "z": float(sign["frame13"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame13"]["left_wrist"]["x"]), 
                "y": float(sign["frame13"]["left_wrist"]["y"]), 
                "z": float(sign["frame13"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame13"]["right_wrist"]["x"]), 
                "y": float(sign["frame13"]["right_wrist"]["y"]), 
                "z": float(sign["frame13"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame13"]["left_pinky"]["x"]), 
                "y": float(sign["frame13"]["left_pinky"]["y"]), 
                "z": float(sign["frame13"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame13"]["right_pinky"]["x"]), 
                "y": float(sign["frame13"]["right_pinky"]["y"]), 
                "z": float(sign["frame13"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame13"]["left_index"]["x"]), 
                "y": float(sign["frame13"]["left_index"]["y"]), 
                "z": float(sign["frame13"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame13"]["right_index"]["x"]), 
                "y": float(sign["frame13"]["right_index"]["y"]), 
                "z": float(sign["frame13"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame13"]["left_thumb"]["x"]), 
                "y": float(sign["frame13"]["left_thumb"]["y"]), 
                "z": float(sign["frame13"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame13"]["right_thumb"]["x"]), 
                "y": float(sign["frame13"]["right_thumb"]["y"]), 
                "z": float(sign["frame13"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame13"]["left_hip"]["x"]), 
                "y": float(sign["frame13"]["left_hip"]["y"]), 
                "z": float(sign["frame13"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame13"]["right_hip"]["x"]), 
                "y": float(sign["frame13"]["right_hip"]["y"]), 
                "z": float(sign["frame13"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame13"]["left_knee"]["x"]), 
                "y": float(sign["frame13"]["left_knee"]["y"]), 
                "z": float(sign["frame13"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame13"]["right_knee"]["x"]), 
                "y": float(sign["frame13"]["right_knee"]["y"]), 
                "z": float(sign["frame13"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame13"]["left_ankle"]["x"]), 
                "y": float(sign["frame13"]["left_ankle"]["y"]), 
                "z": float(sign["frame13"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame13"]["right_ankle"]["x"]), 
                "y": float(sign["frame13"]["right_ankle"]["y"]), 
                "z": float(sign["frame13"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame13"]["left_heel"]["x"]), 
                "y": float(sign["frame13"]["left_heel"]["y"]), 
                "z": float(sign["frame13"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame13"]["right_heel"]["x"]), 
                "y": float(sign["frame13"]["right_heel"]["y"]), 
                "z": float(sign["frame13"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame13"]["left_foot_index"]["x"]), 
                "y": float(sign["frame13"]["left_foot_index"]["y"]), 
                "z": float(sign["frame13"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame13"]["right_foot_index"]["x"]), 
                "y": float(sign["frame13"]["right_foot_index"]["y"]), 
                "z": float(sign["frame13"]["right_foot_index"]["z"])
            },
        },
                "frame14": {
            "nose": {
                "x": float(sign["frame14"]["nose"]["x"]), 
                "y": float(sign["frame14"]["nose"]["y"]), 
                "z": float(sign["frame14"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame14"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame14"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame14"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame14"]["left_eye"]["x"]), 
                "y": float(sign["frame14"]["left_eye"]["y"]), 
                "z": float(sign["frame14"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame14"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame14"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame14"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame14"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame14"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame14"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame14"]["right_eye"]["x"]), 
                "y": float(sign["frame14"]["right_eye"]["y"]), 
                "z": float(sign["frame14"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame14"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame14"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame14"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame14"]["left_ear"]["x"]), 
                "y": float(sign["frame14"]["left_ear"]["y"]), 
                "z": float(sign["frame14"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame14"]["right_ear"]["x"]), 
                "y": float(sign["frame14"]["right_ear"]["y"]), 
                "z": float(sign["frame14"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame14"]["mouth_left"]["x"]), 
                "y": float(sign["frame14"]["mouth_left"]["y"]), 
                "z": float(sign["frame14"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame14"]["mouth_right"]["x"]), 
                "y": float(sign["frame14"]["mouth_right"]["y"]), 
                "z": float(sign["frame14"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame14"]["left_shoulder"]["x"]), 
                "y": float(sign["frame14"]["left_shoulder"]["y"]), 
                "z": float(sign["frame14"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame14"]["right_shoulder"]["x"]), 
                "y": float(sign["frame14"]["right_shoulder"]["y"]), 
                "z": float(sign["frame14"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame14"]["left_elbow"]["x"]), 
                "y": float(sign["frame14"]["left_elbow"]["y"]), 
                "z": float(sign["frame14"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame14"]["right_elbow"]["x"]), 
                "y": float(sign["frame14"]["right_elbow"]["y"]), 
                "z": float(sign["frame14"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame14"]["left_wrist"]["x"]), 
                "y": float(sign["frame14"]["left_wrist"]["y"]), 
                "z": float(sign["frame14"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame14"]["right_wrist"]["x"]), 
                "y": float(sign["frame14"]["right_wrist"]["y"]), 
                "z": float(sign["frame14"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame14"]["left_pinky"]["x"]), 
                "y": float(sign["frame14"]["left_pinky"]["y"]), 
                "z": float(sign["frame14"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame14"]["right_pinky"]["x"]), 
                "y": float(sign["frame14"]["right_pinky"]["y"]), 
                "z": float(sign["frame14"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame14"]["left_index"]["x"]), 
                "y": float(sign["frame14"]["left_index"]["y"]), 
                "z": float(sign["frame14"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame14"]["right_index"]["x"]), 
                "y": float(sign["frame14"]["right_index"]["y"]), 
                "z": float(sign["frame14"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame14"]["left_thumb"]["x"]), 
                "y": float(sign["frame14"]["left_thumb"]["y"]), 
                "z": float(sign["frame14"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame14"]["right_thumb"]["x"]), 
                "y": float(sign["frame14"]["right_thumb"]["y"]), 
                "z": float(sign["frame14"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame14"]["left_hip"]["x"]), 
                "y": float(sign["frame14"]["left_hip"]["y"]), 
                "z": float(sign["frame14"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame14"]["right_hip"]["x"]), 
                "y": float(sign["frame14"]["right_hip"]["y"]), 
                "z": float(sign["frame14"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame14"]["left_knee"]["x"]), 
                "y": float(sign["frame14"]["left_knee"]["y"]), 
                "z": float(sign["frame14"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame14"]["right_knee"]["x"]), 
                "y": float(sign["frame14"]["right_knee"]["y"]), 
                "z": float(sign["frame14"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame14"]["left_ankle"]["x"]), 
                "y": float(sign["frame14"]["left_ankle"]["y"]), 
                "z": float(sign["frame14"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame14"]["right_ankle"]["x"]), 
                "y": float(sign["frame14"]["right_ankle"]["y"]), 
                "z": float(sign["frame14"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame14"]["left_heel"]["x"]), 
                "y": float(sign["frame14"]["left_heel"]["y"]), 
                "z": float(sign["frame14"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame14"]["right_heel"]["x"]), 
                "y": float(sign["frame14"]["right_heel"]["y"]), 
                "z": float(sign["frame14"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame14"]["left_foot_index"]["x"]), 
                "y": float(sign["frame14"]["left_foot_index"]["y"]), 
                "z": float(sign["frame14"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame14"]["right_foot_index"]["x"]), 
                "y": float(sign["frame14"]["right_foot_index"]["y"]), 
                "z": float(sign["frame14"]["right_foot_index"]["z"])
            },
        },
                "frame15": {
            "nose": {
                "x": float(sign["frame15"]["nose"]["x"]), 
                "y": float(sign["frame15"]["nose"]["y"]), 
                "z": float(sign["frame15"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame15"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame15"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame15"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame15"]["left_eye"]["x"]), 
                "y": float(sign["frame15"]["left_eye"]["y"]), 
                "z": float(sign["frame15"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame15"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame15"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame15"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame15"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame15"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame15"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame15"]["right_eye"]["x"]), 
                "y": float(sign["frame15"]["right_eye"]["y"]), 
                "z": float(sign["frame15"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame15"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame15"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame15"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame15"]["left_ear"]["x"]), 
                "y": float(sign["frame15"]["left_ear"]["y"]), 
                "z": float(sign["frame15"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame15"]["right_ear"]["x"]), 
                "y": float(sign["frame15"]["right_ear"]["y"]), 
                "z": float(sign["frame15"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame15"]["mouth_left"]["x"]), 
                "y": float(sign["frame15"]["mouth_left"]["y"]), 
                "z": float(sign["frame15"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame15"]["mouth_right"]["x"]), 
                "y": float(sign["frame15"]["mouth_right"]["y"]), 
                "z": float(sign["frame15"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame15"]["left_shoulder"]["x"]), 
                "y": float(sign["frame15"]["left_shoulder"]["y"]), 
                "z": float(sign["frame15"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame15"]["right_shoulder"]["x"]), 
                "y": float(sign["frame15"]["right_shoulder"]["y"]), 
                "z": float(sign["frame15"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame15"]["left_elbow"]["x"]), 
                "y": float(sign["frame15"]["left_elbow"]["y"]), 
                "z": float(sign["frame15"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame15"]["right_elbow"]["x"]), 
                "y": float(sign["frame15"]["right_elbow"]["y"]), 
                "z": float(sign["frame15"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame15"]["left_wrist"]["x"]), 
                "y": float(sign["frame15"]["left_wrist"]["y"]), 
                "z": float(sign["frame15"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame15"]["right_wrist"]["x"]), 
                "y": float(sign["frame15"]["right_wrist"]["y"]), 
                "z": float(sign["frame15"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame15"]["left_pinky"]["x"]), 
                "y": float(sign["frame15"]["left_pinky"]["y"]), 
                "z": float(sign["frame15"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame15"]["right_pinky"]["x"]), 
                "y": float(sign["frame15"]["right_pinky"]["y"]), 
                "z": float(sign["frame15"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame15"]["left_index"]["x"]), 
                "y": float(sign["frame15"]["left_index"]["y"]), 
                "z": float(sign["frame15"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame15"]["right_index"]["x"]), 
                "y": float(sign["frame15"]["right_index"]["y"]), 
                "z": float(sign["frame15"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame15"]["left_thumb"]["x"]), 
                "y": float(sign["frame15"]["left_thumb"]["y"]), 
                "z": float(sign["frame15"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame15"]["right_thumb"]["x"]), 
                "y": float(sign["frame15"]["right_thumb"]["y"]), 
                "z": float(sign["frame15"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame15"]["left_hip"]["x"]), 
                "y": float(sign["frame15"]["left_hip"]["y"]), 
                "z": float(sign["frame15"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame15"]["right_hip"]["x"]), 
                "y": float(sign["frame15"]["right_hip"]["y"]), 
                "z": float(sign["frame15"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame15"]["left_knee"]["x"]), 
                "y": float(sign["frame15"]["left_knee"]["y"]), 
                "z": float(sign["frame15"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame15"]["right_knee"]["x"]), 
                "y": float(sign["frame15"]["right_knee"]["y"]), 
                "z": float(sign["frame15"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame15"]["left_ankle"]["x"]), 
                "y": float(sign["frame15"]["left_ankle"]["y"]), 
                "z": float(sign["frame15"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame15"]["right_ankle"]["x"]), 
                "y": float(sign["frame15"]["right_ankle"]["y"]), 
                "z": float(sign["frame15"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame15"]["left_heel"]["x"]), 
                "y": float(sign["frame15"]["left_heel"]["y"]), 
                "z": float(sign["frame15"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame15"]["right_heel"]["x"]), 
                "y": float(sign["frame15"]["right_heel"]["y"]), 
                "z": float(sign["frame15"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame15"]["left_foot_index"]["x"]), 
                "y": float(sign["frame15"]["left_foot_index"]["y"]), 
                "z": float(sign["frame15"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame15"]["right_foot_index"]["x"]), 
                "y": float(sign["frame15"]["right_foot_index"]["y"]), 
                "z": float(sign["frame15"]["right_foot_index"]["z"])
            },
        },
                "frame16": {
            "nose": {
                "x": float(sign["frame16"]["nose"]["x"]), 
                "y": float(sign["frame16"]["nose"]["y"]), 
                "z": float(sign["frame16"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame16"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame16"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame16"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame16"]["left_eye"]["x"]), 
                "y": float(sign["frame16"]["left_eye"]["y"]), 
                "z": float(sign["frame16"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame16"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame16"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame16"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame16"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame16"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame16"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame16"]["right_eye"]["x"]), 
                "y": float(sign["frame16"]["right_eye"]["y"]), 
                "z": float(sign["frame16"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame16"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame16"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame16"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame16"]["left_ear"]["x"]), 
                "y": float(sign["frame16"]["left_ear"]["y"]), 
                "z": float(sign["frame16"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame16"]["right_ear"]["x"]), 
                "y": float(sign["frame16"]["right_ear"]["y"]), 
                "z": float(sign["frame16"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame16"]["mouth_left"]["x"]), 
                "y": float(sign["frame16"]["mouth_left"]["y"]), 
                "z": float(sign["frame16"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame16"]["mouth_right"]["x"]), 
                "y": float(sign["frame16"]["mouth_right"]["y"]), 
                "z": float(sign["frame16"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame16"]["left_shoulder"]["x"]), 
                "y": float(sign["frame16"]["left_shoulder"]["y"]), 
                "z": float(sign["frame16"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame16"]["right_shoulder"]["x"]), 
                "y": float(sign["frame16"]["right_shoulder"]["y"]), 
                "z": float(sign["frame16"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame16"]["left_elbow"]["x"]), 
                "y": float(sign["frame16"]["left_elbow"]["y"]), 
                "z": float(sign["frame16"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame16"]["right_elbow"]["x"]), 
                "y": float(sign["frame16"]["right_elbow"]["y"]), 
                "z": float(sign["frame16"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame16"]["left_wrist"]["x"]), 
                "y": float(sign["frame16"]["left_wrist"]["y"]), 
                "z": float(sign["frame16"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame16"]["right_wrist"]["x"]), 
                "y": float(sign["frame16"]["right_wrist"]["y"]), 
                "z": float(sign["frame16"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame16"]["left_pinky"]["x"]), 
                "y": float(sign["frame16"]["left_pinky"]["y"]), 
                "z": float(sign["frame16"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame16"]["right_pinky"]["x"]), 
                "y": float(sign["frame16"]["right_pinky"]["y"]), 
                "z": float(sign["frame16"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame16"]["left_index"]["x"]), 
                "y": float(sign["frame16"]["left_index"]["y"]), 
                "z": float(sign["frame16"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame16"]["right_index"]["x"]), 
                "y": float(sign["frame16"]["right_index"]["y"]), 
                "z": float(sign["frame16"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame16"]["left_thumb"]["x"]), 
                "y": float(sign["frame16"]["left_thumb"]["y"]), 
                "z": float(sign["frame16"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame16"]["right_thumb"]["x"]), 
                "y": float(sign["frame16"]["right_thumb"]["y"]), 
                "z": float(sign["frame16"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame16"]["left_hip"]["x"]), 
                "y": float(sign["frame16"]["left_hip"]["y"]), 
                "z": float(sign["frame16"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame16"]["right_hip"]["x"]), 
                "y": float(sign["frame16"]["right_hip"]["y"]), 
                "z": float(sign["frame16"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame16"]["left_knee"]["x"]), 
                "y": float(sign["frame16"]["left_knee"]["y"]), 
                "z": float(sign["frame16"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame16"]["right_knee"]["x"]), 
                "y": float(sign["frame16"]["right_knee"]["y"]), 
                "z": float(sign["frame16"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame16"]["left_ankle"]["x"]), 
                "y": float(sign["frame16"]["left_ankle"]["y"]), 
                "z": float(sign["frame16"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame16"]["right_ankle"]["x"]), 
                "y": float(sign["frame16"]["right_ankle"]["y"]), 
                "z": float(sign["frame16"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame16"]["left_heel"]["x"]), 
                "y": float(sign["frame16"]["left_heel"]["y"]), 
                "z": float(sign["frame16"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame16"]["right_heel"]["x"]), 
                "y": float(sign["frame16"]["right_heel"]["y"]), 
                "z": float(sign["frame16"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame16"]["left_foot_index"]["x"]), 
                "y": float(sign["frame16"]["left_foot_index"]["y"]), 
                "z": float(sign["frame16"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame16"]["right_foot_index"]["x"]), 
                "y": float(sign["frame16"]["right_foot_index"]["y"]), 
                "z": float(sign["frame16"]["right_foot_index"]["z"])
            },
        },
                "frame17": {
            "nose": {
                "x": float(sign["frame17"]["nose"]["x"]), 
                "y": float(sign["frame17"]["nose"]["y"]), 
                "z": float(sign["frame17"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame17"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame17"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame17"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame17"]["left_eye"]["x"]), 
                "y": float(sign["frame17"]["left_eye"]["y"]), 
                "z": float(sign["frame17"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame17"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame17"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame17"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame17"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame17"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame17"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame17"]["right_eye"]["x"]), 
                "y": float(sign["frame17"]["right_eye"]["y"]), 
                "z": float(sign["frame17"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame17"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame17"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame17"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame17"]["left_ear"]["x"]), 
                "y": float(sign["frame17"]["left_ear"]["y"]), 
                "z": float(sign["frame17"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame17"]["right_ear"]["x"]), 
                "y": float(sign["frame17"]["right_ear"]["y"]), 
                "z": float(sign["frame17"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame17"]["mouth_left"]["x"]), 
                "y": float(sign["frame17"]["mouth_left"]["y"]), 
                "z": float(sign["frame17"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame17"]["mouth_right"]["x"]), 
                "y": float(sign["frame17"]["mouth_right"]["y"]), 
                "z": float(sign["frame17"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame17"]["left_shoulder"]["x"]), 
                "y": float(sign["frame17"]["left_shoulder"]["y"]), 
                "z": float(sign["frame17"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame17"]["right_shoulder"]["x"]), 
                "y": float(sign["frame17"]["right_shoulder"]["y"]), 
                "z": float(sign["frame17"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame17"]["left_elbow"]["x"]), 
                "y": float(sign["frame17"]["left_elbow"]["y"]), 
                "z": float(sign["frame17"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame17"]["right_elbow"]["x"]), 
                "y": float(sign["frame17"]["right_elbow"]["y"]), 
                "z": float(sign["frame17"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame17"]["left_wrist"]["x"]), 
                "y": float(sign["frame17"]["left_wrist"]["y"]), 
                "z": float(sign["frame17"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame17"]["right_wrist"]["x"]), 
                "y": float(sign["frame17"]["right_wrist"]["y"]), 
                "z": float(sign["frame17"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame17"]["left_pinky"]["x"]), 
                "y": float(sign["frame17"]["left_pinky"]["y"]), 
                "z": float(sign["frame17"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame17"]["right_pinky"]["x"]), 
                "y": float(sign["frame17"]["right_pinky"]["y"]), 
                "z": float(sign["frame17"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame17"]["left_index"]["x"]), 
                "y": float(sign["frame17"]["left_index"]["y"]), 
                "z": float(sign["frame17"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame17"]["right_index"]["x"]), 
                "y": float(sign["frame17"]["right_index"]["y"]), 
                "z": float(sign["frame17"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame17"]["left_thumb"]["x"]), 
                "y": float(sign["frame17"]["left_thumb"]["y"]), 
                "z": float(sign["frame17"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame17"]["right_thumb"]["x"]), 
                "y": float(sign["frame17"]["right_thumb"]["y"]), 
                "z": float(sign["frame17"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame17"]["left_hip"]["x"]), 
                "y": float(sign["frame17"]["left_hip"]["y"]), 
                "z": float(sign["frame17"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame17"]["right_hip"]["x"]), 
                "y": float(sign["frame17"]["right_hip"]["y"]), 
                "z": float(sign["frame17"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame17"]["left_knee"]["x"]), 
                "y": float(sign["frame17"]["left_knee"]["y"]), 
                "z": float(sign["frame17"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame17"]["right_knee"]["x"]), 
                "y": float(sign["frame17"]["right_knee"]["y"]), 
                "z": float(sign["frame17"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame17"]["left_ankle"]["x"]), 
                "y": float(sign["frame17"]["left_ankle"]["y"]), 
                "z": float(sign["frame17"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame17"]["right_ankle"]["x"]), 
                "y": float(sign["frame17"]["right_ankle"]["y"]), 
                "z": float(sign["frame17"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame17"]["left_heel"]["x"]), 
                "y": float(sign["frame17"]["left_heel"]["y"]), 
                "z": float(sign["frame17"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame17"]["right_heel"]["x"]), 
                "y": float(sign["frame17"]["right_heel"]["y"]), 
                "z": float(sign["frame17"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame17"]["left_foot_index"]["x"]), 
                "y": float(sign["frame17"]["left_foot_index"]["y"]), 
                "z": float(sign["frame17"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame17"]["right_foot_index"]["x"]), 
                "y": float(sign["frame17"]["right_foot_index"]["y"]), 
                "z": float(sign["frame17"]["right_foot_index"]["z"])
            },
        },
                "frame18": {
            "nose": {
                "x": float(sign["frame18"]["nose"]["x"]), 
                "y": float(sign["frame18"]["nose"]["y"]), 
                "z": float(sign["frame18"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame18"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame18"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame18"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame18"]["left_eye"]["x"]), 
                "y": float(sign["frame18"]["left_eye"]["y"]), 
                "z": float(sign["frame18"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame18"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame18"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame18"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame18"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame18"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame18"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame18"]["right_eye"]["x"]), 
                "y": float(sign["frame18"]["right_eye"]["y"]), 
                "z": float(sign["frame18"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame18"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame18"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame18"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame18"]["left_ear"]["x"]), 
                "y": float(sign["frame18"]["left_ear"]["y"]), 
                "z": float(sign["frame18"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame18"]["right_ear"]["x"]), 
                "y": float(sign["frame18"]["right_ear"]["y"]), 
                "z": float(sign["frame18"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame18"]["mouth_left"]["x"]), 
                "y": float(sign["frame18"]["mouth_left"]["y"]), 
                "z": float(sign["frame18"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame18"]["mouth_right"]["x"]), 
                "y": float(sign["frame18"]["mouth_right"]["y"]), 
                "z": float(sign["frame18"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame18"]["left_shoulder"]["x"]), 
                "y": float(sign["frame18"]["left_shoulder"]["y"]), 
                "z": float(sign["frame18"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame18"]["right_shoulder"]["x"]), 
                "y": float(sign["frame18"]["right_shoulder"]["y"]), 
                "z": float(sign["frame18"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame18"]["left_elbow"]["x"]), 
                "y": float(sign["frame18"]["left_elbow"]["y"]), 
                "z": float(sign["frame18"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame18"]["right_elbow"]["x"]), 
                "y": float(sign["frame18"]["right_elbow"]["y"]), 
                "z": float(sign["frame18"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame18"]["left_wrist"]["x"]), 
                "y": float(sign["frame18"]["left_wrist"]["y"]), 
                "z": float(sign["frame18"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame18"]["right_wrist"]["x"]), 
                "y": float(sign["frame18"]["right_wrist"]["y"]), 
                "z": float(sign["frame18"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame18"]["left_pinky"]["x"]), 
                "y": float(sign["frame18"]["left_pinky"]["y"]), 
                "z": float(sign["frame18"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame18"]["right_pinky"]["x"]), 
                "y": float(sign["frame18"]["right_pinky"]["y"]), 
                "z": float(sign["frame18"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame18"]["left_index"]["x"]), 
                "y": float(sign["frame18"]["left_index"]["y"]), 
                "z": float(sign["frame18"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame18"]["right_index"]["x"]), 
                "y": float(sign["frame18"]["right_index"]["y"]), 
                "z": float(sign["frame18"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame18"]["left_thumb"]["x"]), 
                "y": float(sign["frame18"]["left_thumb"]["y"]), 
                "z": float(sign["frame18"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame18"]["right_thumb"]["x"]), 
                "y": float(sign["frame18"]["right_thumb"]["y"]), 
                "z": float(sign["frame18"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame18"]["left_hip"]["x"]), 
                "y": float(sign["frame18"]["left_hip"]["y"]), 
                "z": float(sign["frame18"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame18"]["right_hip"]["x"]), 
                "y": float(sign["frame18"]["right_hip"]["y"]), 
                "z": float(sign["frame18"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame18"]["left_knee"]["x"]), 
                "y": float(sign["frame18"]["left_knee"]["y"]), 
                "z": float(sign["frame18"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame18"]["right_knee"]["x"]), 
                "y": float(sign["frame18"]["right_knee"]["y"]), 
                "z": float(sign["frame18"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame18"]["left_ankle"]["x"]), 
                "y": float(sign["frame18"]["left_ankle"]["y"]), 
                "z": float(sign["frame18"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame18"]["right_ankle"]["x"]), 
                "y": float(sign["frame18"]["right_ankle"]["y"]), 
                "z": float(sign["frame18"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame18"]["left_heel"]["x"]), 
                "y": float(sign["frame18"]["left_heel"]["y"]), 
                "z": float(sign["frame18"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame18"]["right_heel"]["x"]), 
                "y": float(sign["frame18"]["right_heel"]["y"]), 
                "z": float(sign["frame18"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame18"]["left_foot_index"]["x"]), 
                "y": float(sign["frame18"]["left_foot_index"]["y"]), 
                "z": float(sign["frame18"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame18"]["right_foot_index"]["x"]), 
                "y": float(sign["frame18"]["right_foot_index"]["y"]), 
                "z": float(sign["frame18"]["right_foot_index"]["z"])
            },
        },
                "frame19": {
            "nose": {
                "x": float(sign["frame19"]["nose"]["x"]), 
                "y": float(sign["frame19"]["nose"]["y"]), 
                "z": float(sign["frame19"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame19"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame19"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame19"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame19"]["left_eye"]["x"]), 
                "y": float(sign["frame19"]["left_eye"]["y"]), 
                "z": float(sign["frame19"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame19"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame19"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame19"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame19"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame19"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame19"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame19"]["right_eye"]["x"]), 
                "y": float(sign["frame19"]["right_eye"]["y"]), 
                "z": float(sign["frame19"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame19"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame19"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame19"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame19"]["left_ear"]["x"]), 
                "y": float(sign["frame19"]["left_ear"]["y"]), 
                "z": float(sign["frame19"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame19"]["right_ear"]["x"]), 
                "y": float(sign["frame19"]["right_ear"]["y"]), 
                "z": float(sign["frame19"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame19"]["mouth_left"]["x"]), 
                "y": float(sign["frame19"]["mouth_left"]["y"]), 
                "z": float(sign["frame19"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame19"]["mouth_right"]["x"]), 
                "y": float(sign["frame19"]["mouth_right"]["y"]), 
                "z": float(sign["frame19"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame19"]["left_shoulder"]["x"]), 
                "y": float(sign["frame19"]["left_shoulder"]["y"]), 
                "z": float(sign["frame19"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame19"]["right_shoulder"]["x"]), 
                "y": float(sign["frame19"]["right_shoulder"]["y"]), 
                "z": float(sign["frame19"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame19"]["left_elbow"]["x"]), 
                "y": float(sign["frame19"]["left_elbow"]["y"]), 
                "z": float(sign["frame19"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame19"]["right_elbow"]["x"]), 
                "y": float(sign["frame19"]["right_elbow"]["y"]), 
                "z": float(sign["frame19"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame19"]["left_wrist"]["x"]), 
                "y": float(sign["frame19"]["left_wrist"]["y"]), 
                "z": float(sign["frame19"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame19"]["right_wrist"]["x"]), 
                "y": float(sign["frame19"]["right_wrist"]["y"]), 
                "z": float(sign["frame19"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame19"]["left_pinky"]["x"]), 
                "y": float(sign["frame19"]["left_pinky"]["y"]), 
                "z": float(sign["frame19"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame19"]["right_pinky"]["x"]), 
                "y": float(sign["frame19"]["right_pinky"]["y"]), 
                "z": float(sign["frame19"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame19"]["left_index"]["x"]), 
                "y": float(sign["frame19"]["left_index"]["y"]), 
                "z": float(sign["frame19"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame19"]["right_index"]["x"]), 
                "y": float(sign["frame19"]["right_index"]["y"]), 
                "z": float(sign["frame19"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame19"]["left_thumb"]["x"]), 
                "y": float(sign["frame19"]["left_thumb"]["y"]), 
                "z": float(sign["frame19"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame19"]["right_thumb"]["x"]), 
                "y": float(sign["frame19"]["right_thumb"]["y"]), 
                "z": float(sign["frame19"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame19"]["left_hip"]["x"]), 
                "y": float(sign["frame19"]["left_hip"]["y"]), 
                "z": float(sign["frame19"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame19"]["right_hip"]["x"]), 
                "y": float(sign["frame19"]["right_hip"]["y"]), 
                "z": float(sign["frame19"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame19"]["left_knee"]["x"]), 
                "y": float(sign["frame19"]["left_knee"]["y"]), 
                "z": float(sign["frame19"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame19"]["right_knee"]["x"]), 
                "y": float(sign["frame19"]["right_knee"]["y"]), 
                "z": float(sign["frame19"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame19"]["left_ankle"]["x"]), 
                "y": float(sign["frame19"]["left_ankle"]["y"]), 
                "z": float(sign["frame19"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame19"]["right_ankle"]["x"]), 
                "y": float(sign["frame19"]["right_ankle"]["y"]), 
                "z": float(sign["frame19"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame19"]["left_heel"]["x"]), 
                "y": float(sign["frame19"]["left_heel"]["y"]), 
                "z": float(sign["frame19"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame19"]["right_heel"]["x"]), 
                "y": float(sign["frame19"]["right_heel"]["y"]), 
                "z": float(sign["frame19"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame19"]["left_foot_index"]["x"]), 
                "y": float(sign["frame19"]["left_foot_index"]["y"]), 
                "z": float(sign["frame19"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame19"]["right_foot_index"]["x"]), 
                "y": float(sign["frame19"]["right_foot_index"]["y"]), 
                "z": float(sign["frame19"]["right_foot_index"]["z"])
            },
        },
                "frame20": {
            "nose": {
                "x": float(sign["frame20"]["nose"]["x"]), 
                "y": float(sign["frame20"]["nose"]["y"]), 
                "z": float(sign["frame20"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame20"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame20"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame20"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame20"]["left_eye"]["x"]), 
                "y": float(sign["frame20"]["left_eye"]["y"]), 
                "z": float(sign["frame20"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame20"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame20"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame20"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame20"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame20"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame20"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame20"]["right_eye"]["x"]), 
                "y": float(sign["frame20"]["right_eye"]["y"]), 
                "z": float(sign["frame20"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame20"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame20"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame20"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame20"]["left_ear"]["x"]), 
                "y": float(sign["frame20"]["left_ear"]["y"]), 
                "z": float(sign["frame20"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame20"]["right_ear"]["x"]), 
                "y": float(sign["frame20"]["right_ear"]["y"]), 
                "z": float(sign["frame20"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame20"]["mouth_left"]["x"]), 
                "y": float(sign["frame20"]["mouth_left"]["y"]), 
                "z": float(sign["frame20"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame20"]["mouth_right"]["x"]), 
                "y": float(sign["frame20"]["mouth_right"]["y"]), 
                "z": float(sign["frame20"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame20"]["left_shoulder"]["x"]), 
                "y": float(sign["frame20"]["left_shoulder"]["y"]), 
                "z": float(sign["frame20"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame20"]["right_shoulder"]["x"]), 
                "y": float(sign["frame20"]["right_shoulder"]["y"]), 
                "z": float(sign["frame20"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame20"]["left_elbow"]["x"]), 
                "y": float(sign["frame20"]["left_elbow"]["y"]), 
                "z": float(sign["frame20"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame20"]["right_elbow"]["x"]), 
                "y": float(sign["frame20"]["right_elbow"]["y"]), 
                "z": float(sign["frame20"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame20"]["left_wrist"]["x"]), 
                "y": float(sign["frame20"]["left_wrist"]["y"]), 
                "z": float(sign["frame20"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame20"]["right_wrist"]["x"]), 
                "y": float(sign["frame20"]["right_wrist"]["y"]), 
                "z": float(sign["frame20"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame20"]["left_pinky"]["x"]), 
                "y": float(sign["frame20"]["left_pinky"]["y"]), 
                "z": float(sign["frame20"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame20"]["right_pinky"]["x"]), 
                "y": float(sign["frame20"]["right_pinky"]["y"]), 
                "z": float(sign["frame20"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame20"]["left_index"]["x"]), 
                "y": float(sign["frame20"]["left_index"]["y"]), 
                "z": float(sign["frame20"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame20"]["right_index"]["x"]), 
                "y": float(sign["frame20"]["right_index"]["y"]), 
                "z": float(sign["frame20"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame20"]["left_thumb"]["x"]), 
                "y": float(sign["frame20"]["left_thumb"]["y"]), 
                "z": float(sign["frame20"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame20"]["right_thumb"]["x"]), 
                "y": float(sign["frame20"]["right_thumb"]["y"]), 
                "z": float(sign["frame20"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame20"]["left_hip"]["x"]), 
                "y": float(sign["frame20"]["left_hip"]["y"]), 
                "z": float(sign["frame20"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame20"]["right_hip"]["x"]), 
                "y": float(sign["frame20"]["right_hip"]["y"]), 
                "z": float(sign["frame20"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame20"]["left_knee"]["x"]), 
                "y": float(sign["frame20"]["left_knee"]["y"]), 
                "z": float(sign["frame20"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame20"]["right_knee"]["x"]), 
                "y": float(sign["frame20"]["right_knee"]["y"]), 
                "z": float(sign["frame20"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame20"]["left_ankle"]["x"]), 
                "y": float(sign["frame20"]["left_ankle"]["y"]), 
                "z": float(sign["frame20"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame20"]["right_ankle"]["x"]), 
                "y": float(sign["frame20"]["right_ankle"]["y"]), 
                "z": float(sign["frame20"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame20"]["left_heel"]["x"]), 
                "y": float(sign["frame20"]["left_heel"]["y"]), 
                "z": float(sign["frame20"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame20"]["right_heel"]["x"]), 
                "y": float(sign["frame20"]["right_heel"]["y"]), 
                "z": float(sign["frame20"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame20"]["left_foot_index"]["x"]), 
                "y": float(sign["frame20"]["left_foot_index"]["y"]), 
                "z": float(sign["frame20"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame20"]["right_foot_index"]["x"]), 
                "y": float(sign["frame20"]["right_foot_index"]["y"]), 
                "z": float(sign["frame20"]["right_foot_index"]["z"])
            },
        },
                "frame21": {
            "nose": {
                "x": float(sign["frame21"]["nose"]["x"]), 
                "y": float(sign["frame21"]["nose"]["y"]), 
                "z": float(sign["frame21"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame21"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame21"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame21"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame21"]["left_eye"]["x"]), 
                "y": float(sign["frame21"]["left_eye"]["y"]), 
                "z": float(sign["frame21"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame21"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame21"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame21"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame21"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame21"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame21"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame21"]["right_eye"]["x"]), 
                "y": float(sign["frame21"]["right_eye"]["y"]), 
                "z": float(sign["frame21"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame21"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame21"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame21"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame21"]["left_ear"]["x"]), 
                "y": float(sign["frame21"]["left_ear"]["y"]), 
                "z": float(sign["frame21"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame21"]["right_ear"]["x"]), 
                "y": float(sign["frame21"]["right_ear"]["y"]), 
                "z": float(sign["frame21"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame21"]["mouth_left"]["x"]), 
                "y": float(sign["frame21"]["mouth_left"]["y"]), 
                "z": float(sign["frame21"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame21"]["mouth_right"]["x"]), 
                "y": float(sign["frame21"]["mouth_right"]["y"]), 
                "z": float(sign["frame21"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame21"]["left_shoulder"]["x"]), 
                "y": float(sign["frame21"]["left_shoulder"]["y"]), 
                "z": float(sign["frame21"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame21"]["right_shoulder"]["x"]), 
                "y": float(sign["frame21"]["right_shoulder"]["y"]), 
                "z": float(sign["frame21"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame21"]["left_elbow"]["x"]), 
                "y": float(sign["frame21"]["left_elbow"]["y"]), 
                "z": float(sign["frame21"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame21"]["right_elbow"]["x"]), 
                "y": float(sign["frame21"]["right_elbow"]["y"]), 
                "z": float(sign["frame21"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame21"]["left_wrist"]["x"]), 
                "y": float(sign["frame21"]["left_wrist"]["y"]), 
                "z": float(sign["frame21"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame21"]["right_wrist"]["x"]), 
                "y": float(sign["frame21"]["right_wrist"]["y"]), 
                "z": float(sign["frame21"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame21"]["left_pinky"]["x"]), 
                "y": float(sign["frame21"]["left_pinky"]["y"]), 
                "z": float(sign["frame21"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame21"]["right_pinky"]["x"]), 
                "y": float(sign["frame21"]["right_pinky"]["y"]), 
                "z": float(sign["frame21"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame21"]["left_index"]["x"]), 
                "y": float(sign["frame21"]["left_index"]["y"]), 
                "z": float(sign["frame21"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame21"]["right_index"]["x"]), 
                "y": float(sign["frame21"]["right_index"]["y"]), 
                "z": float(sign["frame21"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame21"]["left_thumb"]["x"]), 
                "y": float(sign["frame21"]["left_thumb"]["y"]), 
                "z": float(sign["frame21"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame21"]["right_thumb"]["x"]), 
                "y": float(sign["frame21"]["right_thumb"]["y"]), 
                "z": float(sign["frame21"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame21"]["left_hip"]["x"]), 
                "y": float(sign["frame21"]["left_hip"]["y"]), 
                "z": float(sign["frame21"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame21"]["right_hip"]["x"]), 
                "y": float(sign["frame21"]["right_hip"]["y"]), 
                "z": float(sign["frame21"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame21"]["left_knee"]["x"]), 
                "y": float(sign["frame21"]["left_knee"]["y"]), 
                "z": float(sign["frame21"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame21"]["right_knee"]["x"]), 
                "y": float(sign["frame21"]["right_knee"]["y"]), 
                "z": float(sign["frame21"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame21"]["left_ankle"]["x"]), 
                "y": float(sign["frame21"]["left_ankle"]["y"]), 
                "z": float(sign["frame21"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame21"]["right_ankle"]["x"]), 
                "y": float(sign["frame21"]["right_ankle"]["y"]), 
                "z": float(sign["frame21"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame21"]["left_heel"]["x"]), 
                "y": float(sign["frame21"]["left_heel"]["y"]), 
                "z": float(sign["frame21"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame21"]["right_heel"]["x"]), 
                "y": float(sign["frame21"]["right_heel"]["y"]), 
                "z": float(sign["frame21"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame21"]["left_foot_index"]["x"]), 
                "y": float(sign["frame21"]["left_foot_index"]["y"]), 
                "z": float(sign["frame21"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame21"]["right_foot_index"]["x"]), 
                "y": float(sign["frame21"]["right_foot_index"]["y"]), 
                "z": float(sign["frame21"]["right_foot_index"]["z"])
            },
        },
                "frame22": {
            "nose": {
                "x": float(sign["frame22"]["nose"]["x"]), 
                "y": float(sign["frame22"]["nose"]["y"]), 
                "z": float(sign["frame22"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame22"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame22"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame22"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame22"]["left_eye"]["x"]), 
                "y": float(sign["frame22"]["left_eye"]["y"]), 
                "z": float(sign["frame22"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame22"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame22"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame22"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame22"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame22"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame22"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame22"]["right_eye"]["x"]), 
                "y": float(sign["frame22"]["right_eye"]["y"]), 
                "z": float(sign["frame22"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame22"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame22"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame22"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame22"]["left_ear"]["x"]), 
                "y": float(sign["frame22"]["left_ear"]["y"]), 
                "z": float(sign["frame22"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame22"]["right_ear"]["x"]), 
                "y": float(sign["frame22"]["right_ear"]["y"]), 
                "z": float(sign["frame22"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame22"]["mouth_left"]["x"]), 
                "y": float(sign["frame22"]["mouth_left"]["y"]), 
                "z": float(sign["frame22"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame22"]["mouth_right"]["x"]), 
                "y": float(sign["frame22"]["mouth_right"]["y"]), 
                "z": float(sign["frame22"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame22"]["left_shoulder"]["x"]), 
                "y": float(sign["frame22"]["left_shoulder"]["y"]), 
                "z": float(sign["frame22"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame22"]["right_shoulder"]["x"]), 
                "y": float(sign["frame22"]["right_shoulder"]["y"]), 
                "z": float(sign["frame22"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame22"]["left_elbow"]["x"]), 
                "y": float(sign["frame22"]["left_elbow"]["y"]), 
                "z": float(sign["frame22"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame22"]["right_elbow"]["x"]), 
                "y": float(sign["frame22"]["right_elbow"]["y"]), 
                "z": float(sign["frame22"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame22"]["left_wrist"]["x"]), 
                "y": float(sign["frame22"]["left_wrist"]["y"]), 
                "z": float(sign["frame22"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame22"]["right_wrist"]["x"]), 
                "y": float(sign["frame22"]["right_wrist"]["y"]), 
                "z": float(sign["frame22"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame22"]["left_pinky"]["x"]), 
                "y": float(sign["frame22"]["left_pinky"]["y"]), 
                "z": float(sign["frame22"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame22"]["right_pinky"]["x"]), 
                "y": float(sign["frame22"]["right_pinky"]["y"]), 
                "z": float(sign["frame22"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame22"]["left_index"]["x"]), 
                "y": float(sign["frame22"]["left_index"]["y"]), 
                "z": float(sign["frame22"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame22"]["right_index"]["x"]), 
                "y": float(sign["frame22"]["right_index"]["y"]), 
                "z": float(sign["frame22"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame22"]["left_thumb"]["x"]), 
                "y": float(sign["frame22"]["left_thumb"]["y"]), 
                "z": float(sign["frame22"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame22"]["right_thumb"]["x"]), 
                "y": float(sign["frame22"]["right_thumb"]["y"]), 
                "z": float(sign["frame22"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame22"]["left_hip"]["x"]), 
                "y": float(sign["frame22"]["left_hip"]["y"]), 
                "z": float(sign["frame22"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame22"]["right_hip"]["x"]), 
                "y": float(sign["frame22"]["right_hip"]["y"]), 
                "z": float(sign["frame22"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame22"]["left_knee"]["x"]), 
                "y": float(sign["frame22"]["left_knee"]["y"]), 
                "z": float(sign["frame22"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame22"]["right_knee"]["x"]), 
                "y": float(sign["frame22"]["right_knee"]["y"]), 
                "z": float(sign["frame22"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame22"]["left_ankle"]["x"]), 
                "y": float(sign["frame22"]["left_ankle"]["y"]), 
                "z": float(sign["frame22"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame22"]["right_ankle"]["x"]), 
                "y": float(sign["frame22"]["right_ankle"]["y"]), 
                "z": float(sign["frame22"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame22"]["left_heel"]["x"]), 
                "y": float(sign["frame22"]["left_heel"]["y"]), 
                "z": float(sign["frame22"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame22"]["right_heel"]["x"]), 
                "y": float(sign["frame22"]["right_heel"]["y"]), 
                "z": float(sign["frame22"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame22"]["left_foot_index"]["x"]), 
                "y": float(sign["frame22"]["left_foot_index"]["y"]), 
                "z": float(sign["frame22"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame22"]["right_foot_index"]["x"]), 
                "y": float(sign["frame22"]["right_foot_index"]["y"]), 
                "z": float(sign["frame22"]["right_foot_index"]["z"])
            },
        },
                "frame23": {
            "nose": {
                "x": float(sign["frame23"]["nose"]["x"]), 
                "y": float(sign["frame23"]["nose"]["y"]), 
                "z": float(sign["frame23"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame23"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame23"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame23"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame23"]["left_eye"]["x"]), 
                "y": float(sign["frame23"]["left_eye"]["y"]), 
                "z": float(sign["frame23"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame23"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame23"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame23"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame23"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame23"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame23"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame23"]["right_eye"]["x"]), 
                "y": float(sign["frame23"]["right_eye"]["y"]), 
                "z": float(sign["frame23"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame23"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame23"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame23"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame23"]["left_ear"]["x"]), 
                "y": float(sign["frame23"]["left_ear"]["y"]), 
                "z": float(sign["frame23"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame23"]["right_ear"]["x"]), 
                "y": float(sign["frame23"]["right_ear"]["y"]), 
                "z": float(sign["frame23"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame23"]["mouth_left"]["x"]), 
                "y": float(sign["frame23"]["mouth_left"]["y"]), 
                "z": float(sign["frame23"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame23"]["mouth_right"]["x"]), 
                "y": float(sign["frame23"]["mouth_right"]["y"]), 
                "z": float(sign["frame23"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame23"]["left_shoulder"]["x"]), 
                "y": float(sign["frame23"]["left_shoulder"]["y"]), 
                "z": float(sign["frame23"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame23"]["right_shoulder"]["x"]), 
                "y": float(sign["frame23"]["right_shoulder"]["y"]), 
                "z": float(sign["frame23"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame23"]["left_elbow"]["x"]), 
                "y": float(sign["frame23"]["left_elbow"]["y"]), 
                "z": float(sign["frame23"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame23"]["right_elbow"]["x"]), 
                "y": float(sign["frame23"]["right_elbow"]["y"]), 
                "z": float(sign["frame23"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame23"]["left_wrist"]["x"]), 
                "y": float(sign["frame23"]["left_wrist"]["y"]), 
                "z": float(sign["frame23"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame23"]["right_wrist"]["x"]), 
                "y": float(sign["frame23"]["right_wrist"]["y"]), 
                "z": float(sign["frame23"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame23"]["left_pinky"]["x"]), 
                "y": float(sign["frame23"]["left_pinky"]["y"]), 
                "z": float(sign["frame23"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame23"]["right_pinky"]["x"]), 
                "y": float(sign["frame23"]["right_pinky"]["y"]), 
                "z": float(sign["frame23"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame23"]["left_index"]["x"]), 
                "y": float(sign["frame23"]["left_index"]["y"]), 
                "z": float(sign["frame23"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame23"]["right_index"]["x"]), 
                "y": float(sign["frame23"]["right_index"]["y"]), 
                "z": float(sign["frame23"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame23"]["left_thumb"]["x"]), 
                "y": float(sign["frame23"]["left_thumb"]["y"]), 
                "z": float(sign["frame23"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame23"]["right_thumb"]["x"]), 
                "y": float(sign["frame23"]["right_thumb"]["y"]), 
                "z": float(sign["frame23"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame23"]["left_hip"]["x"]), 
                "y": float(sign["frame23"]["left_hip"]["y"]), 
                "z": float(sign["frame23"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame23"]["right_hip"]["x"]), 
                "y": float(sign["frame23"]["right_hip"]["y"]), 
                "z": float(sign["frame23"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame23"]["left_knee"]["x"]), 
                "y": float(sign["frame23"]["left_knee"]["y"]), 
                "z": float(sign["frame23"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame23"]["right_knee"]["x"]), 
                "y": float(sign["frame23"]["right_knee"]["y"]), 
                "z": float(sign["frame23"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame23"]["left_ankle"]["x"]), 
                "y": float(sign["frame23"]["left_ankle"]["y"]), 
                "z": float(sign["frame23"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame23"]["right_ankle"]["x"]), 
                "y": float(sign["frame23"]["right_ankle"]["y"]), 
                "z": float(sign["frame23"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame23"]["left_heel"]["x"]), 
                "y": float(sign["frame23"]["left_heel"]["y"]), 
                "z": float(sign["frame23"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame23"]["right_heel"]["x"]), 
                "y": float(sign["frame23"]["right_heel"]["y"]), 
                "z": float(sign["frame23"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame23"]["left_foot_index"]["x"]), 
                "y": float(sign["frame23"]["left_foot_index"]["y"]), 
                "z": float(sign["frame23"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame23"]["right_foot_index"]["x"]), 
                "y": float(sign["frame23"]["right_foot_index"]["y"]), 
                "z": float(sign["frame23"]["right_foot_index"]["z"])
            },
        },
                "frame24": {
            "nose": {
                "x": float(sign["frame24"]["nose"]["x"]), 
                "y": float(sign["frame24"]["nose"]["y"]), 
                "z": float(sign["frame24"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame24"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame24"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame24"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame24"]["left_eye"]["x"]), 
                "y": float(sign["frame24"]["left_eye"]["y"]), 
                "z": float(sign["frame24"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame24"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame24"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame24"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame24"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame24"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame24"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame24"]["right_eye"]["x"]), 
                "y": float(sign["frame24"]["right_eye"]["y"]), 
                "z": float(sign["frame24"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame24"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame24"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame24"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame24"]["left_ear"]["x"]), 
                "y": float(sign["frame24"]["left_ear"]["y"]), 
                "z": float(sign["frame24"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame24"]["right_ear"]["x"]), 
                "y": float(sign["frame24"]["right_ear"]["y"]), 
                "z": float(sign["frame24"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame24"]["mouth_left"]["x"]), 
                "y": float(sign["frame24"]["mouth_left"]["y"]), 
                "z": float(sign["frame24"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame24"]["mouth_right"]["x"]), 
                "y": float(sign["frame24"]["mouth_right"]["y"]), 
                "z": float(sign["frame24"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame24"]["left_shoulder"]["x"]), 
                "y": float(sign["frame24"]["left_shoulder"]["y"]), 
                "z": float(sign["frame24"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame24"]["right_shoulder"]["x"]), 
                "y": float(sign["frame24"]["right_shoulder"]["y"]), 
                "z": float(sign["frame24"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame24"]["left_elbow"]["x"]), 
                "y": float(sign["frame24"]["left_elbow"]["y"]), 
                "z": float(sign["frame24"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame24"]["right_elbow"]["x"]), 
                "y": float(sign["frame24"]["right_elbow"]["y"]), 
                "z": float(sign["frame24"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame24"]["left_wrist"]["x"]), 
                "y": float(sign["frame24"]["left_wrist"]["y"]), 
                "z": float(sign["frame24"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame24"]["right_wrist"]["x"]), 
                "y": float(sign["frame24"]["right_wrist"]["y"]), 
                "z": float(sign["frame24"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame24"]["left_pinky"]["x"]), 
                "y": float(sign["frame24"]["left_pinky"]["y"]), 
                "z": float(sign["frame24"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame24"]["right_pinky"]["x"]), 
                "y": float(sign["frame24"]["right_pinky"]["y"]), 
                "z": float(sign["frame24"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame24"]["left_index"]["x"]), 
                "y": float(sign["frame24"]["left_index"]["y"]), 
                "z": float(sign["frame24"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame24"]["right_index"]["x"]), 
                "y": float(sign["frame24"]["right_index"]["y"]), 
                "z": float(sign["frame24"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame24"]["left_thumb"]["x"]), 
                "y": float(sign["frame24"]["left_thumb"]["y"]), 
                "z": float(sign["frame24"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame24"]["right_thumb"]["x"]), 
                "y": float(sign["frame24"]["right_thumb"]["y"]), 
                "z": float(sign["frame24"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame24"]["left_hip"]["x"]), 
                "y": float(sign["frame24"]["left_hip"]["y"]), 
                "z": float(sign["frame24"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame24"]["right_hip"]["x"]), 
                "y": float(sign["frame24"]["right_hip"]["y"]), 
                "z": float(sign["frame24"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame24"]["left_knee"]["x"]), 
                "y": float(sign["frame24"]["left_knee"]["y"]), 
                "z": float(sign["frame24"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame24"]["right_knee"]["x"]), 
                "y": float(sign["frame24"]["right_knee"]["y"]), 
                "z": float(sign["frame24"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame24"]["left_ankle"]["x"]), 
                "y": float(sign["frame24"]["left_ankle"]["y"]), 
                "z": float(sign["frame24"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame24"]["right_ankle"]["x"]), 
                "y": float(sign["frame24"]["right_ankle"]["y"]), 
                "z": float(sign["frame24"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame24"]["left_heel"]["x"]), 
                "y": float(sign["frame24"]["left_heel"]["y"]), 
                "z": float(sign["frame24"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame24"]["right_heel"]["x"]), 
                "y": float(sign["frame24"]["right_heel"]["y"]), 
                "z": float(sign["frame24"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame24"]["left_foot_index"]["x"]), 
                "y": float(sign["frame24"]["left_foot_index"]["y"]), 
                "z": float(sign["frame24"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame24"]["right_foot_index"]["x"]), 
                "y": float(sign["frame24"]["right_foot_index"]["y"]), 
                "z": float(sign["frame24"]["right_foot_index"]["z"])
            },
        },
                "frame25": {
            "nose": {
                "x": float(sign["frame25"]["nose"]["x"]), 
                "y": float(sign["frame25"]["nose"]["y"]), 
                "z": float(sign["frame25"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame25"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame25"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame25"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame25"]["left_eye"]["x"]), 
                "y": float(sign["frame25"]["left_eye"]["y"]), 
                "z": float(sign["frame25"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame25"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame25"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame25"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame25"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame25"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame25"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame25"]["right_eye"]["x"]), 
                "y": float(sign["frame25"]["right_eye"]["y"]), 
                "z": float(sign["frame25"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame25"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame25"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame25"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame25"]["left_ear"]["x"]), 
                "y": float(sign["frame25"]["left_ear"]["y"]), 
                "z": float(sign["frame25"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame25"]["right_ear"]["x"]), 
                "y": float(sign["frame25"]["right_ear"]["y"]), 
                "z": float(sign["frame25"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame25"]["mouth_left"]["x"]), 
                "y": float(sign["frame25"]["mouth_left"]["y"]), 
                "z": float(sign["frame25"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame25"]["mouth_right"]["x"]), 
                "y": float(sign["frame25"]["mouth_right"]["y"]), 
                "z": float(sign["frame25"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame25"]["left_shoulder"]["x"]), 
                "y": float(sign["frame25"]["left_shoulder"]["y"]), 
                "z": float(sign["frame25"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame25"]["right_shoulder"]["x"]), 
                "y": float(sign["frame25"]["right_shoulder"]["y"]), 
                "z": float(sign["frame25"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame25"]["left_elbow"]["x"]), 
                "y": float(sign["frame25"]["left_elbow"]["y"]), 
                "z": float(sign["frame25"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame25"]["right_elbow"]["x"]), 
                "y": float(sign["frame25"]["right_elbow"]["y"]), 
                "z": float(sign["frame25"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame25"]["left_wrist"]["x"]), 
                "y": float(sign["frame25"]["left_wrist"]["y"]), 
                "z": float(sign["frame25"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame25"]["right_wrist"]["x"]), 
                "y": float(sign["frame25"]["right_wrist"]["y"]), 
                "z": float(sign["frame25"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame25"]["left_pinky"]["x"]), 
                "y": float(sign["frame25"]["left_pinky"]["y"]), 
                "z": float(sign["frame25"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame25"]["right_pinky"]["x"]), 
                "y": float(sign["frame25"]["right_pinky"]["y"]), 
                "z": float(sign["frame25"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame25"]["left_index"]["x"]), 
                "y": float(sign["frame25"]["left_index"]["y"]), 
                "z": float(sign["frame25"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame25"]["right_index"]["x"]), 
                "y": float(sign["frame25"]["right_index"]["y"]), 
                "z": float(sign["frame25"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame25"]["left_thumb"]["x"]), 
                "y": float(sign["frame25"]["left_thumb"]["y"]), 
                "z": float(sign["frame25"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame25"]["right_thumb"]["x"]), 
                "y": float(sign["frame25"]["right_thumb"]["y"]), 
                "z": float(sign["frame25"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame25"]["left_hip"]["x"]), 
                "y": float(sign["frame25"]["left_hip"]["y"]), 
                "z": float(sign["frame25"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame25"]["right_hip"]["x"]), 
                "y": float(sign["frame25"]["right_hip"]["y"]), 
                "z": float(sign["frame25"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame25"]["left_knee"]["x"]), 
                "y": float(sign["frame25"]["left_knee"]["y"]), 
                "z": float(sign["frame25"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame25"]["right_knee"]["x"]), 
                "y": float(sign["frame25"]["right_knee"]["y"]), 
                "z": float(sign["frame25"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame25"]["left_ankle"]["x"]), 
                "y": float(sign["frame25"]["left_ankle"]["y"]), 
                "z": float(sign["frame25"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame25"]["right_ankle"]["x"]), 
                "y": float(sign["frame25"]["right_ankle"]["y"]), 
                "z": float(sign["frame25"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame25"]["left_heel"]["x"]), 
                "y": float(sign["frame25"]["left_heel"]["y"]), 
                "z": float(sign["frame25"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame25"]["right_heel"]["x"]), 
                "y": float(sign["frame25"]["right_heel"]["y"]), 
                "z": float(sign["frame25"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame25"]["left_foot_index"]["x"]), 
                "y": float(sign["frame25"]["left_foot_index"]["y"]), 
                "z": float(sign["frame25"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame25"]["right_foot_index"]["x"]), 
                "y": float(sign["frame25"]["right_foot_index"]["y"]), 
                "z": float(sign["frame25"]["right_foot_index"]["z"])
            },
        },
                "frame26": {
            "nose": {
                "x": float(sign["frame26"]["nose"]["x"]), 
                "y": float(sign["frame26"]["nose"]["y"]), 
                "z": float(sign["frame26"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame26"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame26"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame26"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame26"]["left_eye"]["x"]), 
                "y": float(sign["frame26"]["left_eye"]["y"]), 
                "z": float(sign["frame26"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame26"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame26"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame26"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame26"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame26"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame26"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame26"]["right_eye"]["x"]), 
                "y": float(sign["frame26"]["right_eye"]["y"]), 
                "z": float(sign["frame26"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame26"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame26"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame26"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame26"]["left_ear"]["x"]), 
                "y": float(sign["frame26"]["left_ear"]["y"]), 
                "z": float(sign["frame26"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame26"]["right_ear"]["x"]), 
                "y": float(sign["frame26"]["right_ear"]["y"]), 
                "z": float(sign["frame26"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame26"]["mouth_left"]["x"]), 
                "y": float(sign["frame26"]["mouth_left"]["y"]), 
                "z": float(sign["frame26"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame26"]["mouth_right"]["x"]), 
                "y": float(sign["frame26"]["mouth_right"]["y"]), 
                "z": float(sign["frame26"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame26"]["left_shoulder"]["x"]), 
                "y": float(sign["frame26"]["left_shoulder"]["y"]), 
                "z": float(sign["frame26"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame26"]["right_shoulder"]["x"]), 
                "y": float(sign["frame26"]["right_shoulder"]["y"]), 
                "z": float(sign["frame26"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame26"]["left_elbow"]["x"]), 
                "y": float(sign["frame26"]["left_elbow"]["y"]), 
                "z": float(sign["frame26"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame26"]["right_elbow"]["x"]), 
                "y": float(sign["frame26"]["right_elbow"]["y"]), 
                "z": float(sign["frame26"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame26"]["left_wrist"]["x"]), 
                "y": float(sign["frame26"]["left_wrist"]["y"]), 
                "z": float(sign["frame26"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame26"]["right_wrist"]["x"]), 
                "y": float(sign["frame26"]["right_wrist"]["y"]), 
                "z": float(sign["frame26"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame26"]["left_pinky"]["x"]), 
                "y": float(sign["frame26"]["left_pinky"]["y"]), 
                "z": float(sign["frame26"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame26"]["right_pinky"]["x"]), 
                "y": float(sign["frame26"]["right_pinky"]["y"]), 
                "z": float(sign["frame26"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame26"]["left_index"]["x"]), 
                "y": float(sign["frame26"]["left_index"]["y"]), 
                "z": float(sign["frame26"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame26"]["right_index"]["x"]), 
                "y": float(sign["frame26"]["right_index"]["y"]), 
                "z": float(sign["frame26"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame26"]["left_thumb"]["x"]), 
                "y": float(sign["frame26"]["left_thumb"]["y"]), 
                "z": float(sign["frame26"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame26"]["right_thumb"]["x"]), 
                "y": float(sign["frame26"]["right_thumb"]["y"]), 
                "z": float(sign["frame26"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame26"]["left_hip"]["x"]), 
                "y": float(sign["frame26"]["left_hip"]["y"]), 
                "z": float(sign["frame26"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame26"]["right_hip"]["x"]), 
                "y": float(sign["frame26"]["right_hip"]["y"]), 
                "z": float(sign["frame26"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame26"]["left_knee"]["x"]), 
                "y": float(sign["frame26"]["left_knee"]["y"]), 
                "z": float(sign["frame26"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame26"]["right_knee"]["x"]), 
                "y": float(sign["frame26"]["right_knee"]["y"]), 
                "z": float(sign["frame26"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame26"]["left_ankle"]["x"]), 
                "y": float(sign["frame26"]["left_ankle"]["y"]), 
                "z": float(sign["frame26"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame26"]["right_ankle"]["x"]), 
                "y": float(sign["frame26"]["right_ankle"]["y"]), 
                "z": float(sign["frame26"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame26"]["left_heel"]["x"]), 
                "y": float(sign["frame26"]["left_heel"]["y"]), 
                "z": float(sign["frame26"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame26"]["right_heel"]["x"]), 
                "y": float(sign["frame26"]["right_heel"]["y"]), 
                "z": float(sign["frame26"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame26"]["left_foot_index"]["x"]), 
                "y": float(sign["frame26"]["left_foot_index"]["y"]), 
                "z": float(sign["frame26"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame26"]["right_foot_index"]["x"]), 
                "y": float(sign["frame26"]["right_foot_index"]["y"]), 
                "z": float(sign["frame26"]["right_foot_index"]["z"])
            },
        },
                "frame27": {
            "nose": {
                "x": float(sign["frame27"]["nose"]["x"]), 
                "y": float(sign["frame27"]["nose"]["y"]), 
                "z": float(sign["frame27"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame27"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame27"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame27"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame27"]["left_eye"]["x"]), 
                "y": float(sign["frame27"]["left_eye"]["y"]), 
                "z": float(sign["frame27"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame27"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame27"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame27"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame27"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame27"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame27"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame27"]["right_eye"]["x"]), 
                "y": float(sign["frame27"]["right_eye"]["y"]), 
                "z": float(sign["frame27"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame27"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame27"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame27"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame27"]["left_ear"]["x"]), 
                "y": float(sign["frame27"]["left_ear"]["y"]), 
                "z": float(sign["frame27"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame27"]["right_ear"]["x"]), 
                "y": float(sign["frame27"]["right_ear"]["y"]), 
                "z": float(sign["frame27"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame27"]["mouth_left"]["x"]), 
                "y": float(sign["frame27"]["mouth_left"]["y"]), 
                "z": float(sign["frame27"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame27"]["mouth_right"]["x"]), 
                "y": float(sign["frame27"]["mouth_right"]["y"]), 
                "z": float(sign["frame27"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame27"]["left_shoulder"]["x"]), 
                "y": float(sign["frame27"]["left_shoulder"]["y"]), 
                "z": float(sign["frame27"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame27"]["right_shoulder"]["x"]), 
                "y": float(sign["frame27"]["right_shoulder"]["y"]), 
                "z": float(sign["frame27"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame27"]["left_elbow"]["x"]), 
                "y": float(sign["frame27"]["left_elbow"]["y"]), 
                "z": float(sign["frame27"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame27"]["right_elbow"]["x"]), 
                "y": float(sign["frame27"]["right_elbow"]["y"]), 
                "z": float(sign["frame27"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame27"]["left_wrist"]["x"]), 
                "y": float(sign["frame27"]["left_wrist"]["y"]), 
                "z": float(sign["frame27"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame27"]["right_wrist"]["x"]), 
                "y": float(sign["frame27"]["right_wrist"]["y"]), 
                "z": float(sign["frame27"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame27"]["left_pinky"]["x"]), 
                "y": float(sign["frame27"]["left_pinky"]["y"]), 
                "z": float(sign["frame27"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame27"]["right_pinky"]["x"]), 
                "y": float(sign["frame27"]["right_pinky"]["y"]), 
                "z": float(sign["frame27"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame27"]["left_index"]["x"]), 
                "y": float(sign["frame27"]["left_index"]["y"]), 
                "z": float(sign["frame27"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame27"]["right_index"]["x"]), 
                "y": float(sign["frame27"]["right_index"]["y"]), 
                "z": float(sign["frame27"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame27"]["left_thumb"]["x"]), 
                "y": float(sign["frame27"]["left_thumb"]["y"]), 
                "z": float(sign["frame27"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame27"]["right_thumb"]["x"]), 
                "y": float(sign["frame27"]["right_thumb"]["y"]), 
                "z": float(sign["frame27"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame27"]["left_hip"]["x"]), 
                "y": float(sign["frame27"]["left_hip"]["y"]), 
                "z": float(sign["frame27"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame27"]["right_hip"]["x"]), 
                "y": float(sign["frame27"]["right_hip"]["y"]), 
                "z": float(sign["frame27"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame27"]["left_knee"]["x"]), 
                "y": float(sign["frame27"]["left_knee"]["y"]), 
                "z": float(sign["frame27"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame27"]["right_knee"]["x"]), 
                "y": float(sign["frame27"]["right_knee"]["y"]), 
                "z": float(sign["frame27"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame27"]["left_ankle"]["x"]), 
                "y": float(sign["frame27"]["left_ankle"]["y"]), 
                "z": float(sign["frame27"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame27"]["right_ankle"]["x"]), 
                "y": float(sign["frame27"]["right_ankle"]["y"]), 
                "z": float(sign["frame27"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame27"]["left_heel"]["x"]), 
                "y": float(sign["frame27"]["left_heel"]["y"]), 
                "z": float(sign["frame27"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame27"]["right_heel"]["x"]), 
                "y": float(sign["frame27"]["right_heel"]["y"]), 
                "z": float(sign["frame27"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame27"]["left_foot_index"]["x"]), 
                "y": float(sign["frame27"]["left_foot_index"]["y"]), 
                "z": float(sign["frame27"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame27"]["right_foot_index"]["x"]), 
                "y": float(sign["frame27"]["right_foot_index"]["y"]), 
                "z": float(sign["frame27"]["right_foot_index"]["z"])
            },
        },
                "frame28": {
            "nose": {
                "x": float(sign["frame28"]["nose"]["x"]), 
                "y": float(sign["frame28"]["nose"]["y"]), 
                "z": float(sign["frame28"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame28"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame28"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame28"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame28"]["left_eye"]["x"]), 
                "y": float(sign["frame28"]["left_eye"]["y"]), 
                "z": float(sign["frame28"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame28"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame28"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame28"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame28"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame28"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame28"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame28"]["right_eye"]["x"]), 
                "y": float(sign["frame28"]["right_eye"]["y"]), 
                "z": float(sign["frame28"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame28"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame28"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame28"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame28"]["left_ear"]["x"]), 
                "y": float(sign["frame28"]["left_ear"]["y"]), 
                "z": float(sign["frame28"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame28"]["right_ear"]["x"]), 
                "y": float(sign["frame28"]["right_ear"]["y"]), 
                "z": float(sign["frame28"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame28"]["mouth_left"]["x"]), 
                "y": float(sign["frame28"]["mouth_left"]["y"]), 
                "z": float(sign["frame28"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame28"]["mouth_right"]["x"]), 
                "y": float(sign["frame28"]["mouth_right"]["y"]), 
                "z": float(sign["frame28"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame28"]["left_shoulder"]["x"]), 
                "y": float(sign["frame28"]["left_shoulder"]["y"]), 
                "z": float(sign["frame28"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame28"]["right_shoulder"]["x"]), 
                "y": float(sign["frame28"]["right_shoulder"]["y"]), 
                "z": float(sign["frame28"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame28"]["left_elbow"]["x"]), 
                "y": float(sign["frame28"]["left_elbow"]["y"]), 
                "z": float(sign["frame28"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame28"]["right_elbow"]["x"]), 
                "y": float(sign["frame28"]["right_elbow"]["y"]), 
                "z": float(sign["frame28"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame28"]["left_wrist"]["x"]), 
                "y": float(sign["frame28"]["left_wrist"]["y"]), 
                "z": float(sign["frame28"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame28"]["right_wrist"]["x"]), 
                "y": float(sign["frame28"]["right_wrist"]["y"]), 
                "z": float(sign["frame28"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame28"]["left_pinky"]["x"]), 
                "y": float(sign["frame28"]["left_pinky"]["y"]), 
                "z": float(sign["frame28"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame28"]["right_pinky"]["x"]), 
                "y": float(sign["frame28"]["right_pinky"]["y"]), 
                "z": float(sign["frame28"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame28"]["left_index"]["x"]), 
                "y": float(sign["frame28"]["left_index"]["y"]), 
                "z": float(sign["frame28"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame28"]["right_index"]["x"]), 
                "y": float(sign["frame28"]["right_index"]["y"]), 
                "z": float(sign["frame28"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame28"]["left_thumb"]["x"]), 
                "y": float(sign["frame28"]["left_thumb"]["y"]), 
                "z": float(sign["frame28"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame28"]["right_thumb"]["x"]), 
                "y": float(sign["frame28"]["right_thumb"]["y"]), 
                "z": float(sign["frame28"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame28"]["left_hip"]["x"]), 
                "y": float(sign["frame28"]["left_hip"]["y"]), 
                "z": float(sign["frame28"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame28"]["right_hip"]["x"]), 
                "y": float(sign["frame28"]["right_hip"]["y"]), 
                "z": float(sign["frame28"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame28"]["left_knee"]["x"]), 
                "y": float(sign["frame28"]["left_knee"]["y"]), 
                "z": float(sign["frame28"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame28"]["right_knee"]["x"]), 
                "y": float(sign["frame28"]["right_knee"]["y"]), 
                "z": float(sign["frame28"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame28"]["left_ankle"]["x"]), 
                "y": float(sign["frame28"]["left_ankle"]["y"]), 
                "z": float(sign["frame28"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame28"]["right_ankle"]["x"]), 
                "y": float(sign["frame28"]["right_ankle"]["y"]), 
                "z": float(sign["frame28"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame28"]["left_heel"]["x"]), 
                "y": float(sign["frame28"]["left_heel"]["y"]), 
                "z": float(sign["frame28"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame28"]["right_heel"]["x"]), 
                "y": float(sign["frame28"]["right_heel"]["y"]), 
                "z": float(sign["frame28"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame28"]["left_foot_index"]["x"]), 
                "y": float(sign["frame28"]["left_foot_index"]["y"]), 
                "z": float(sign["frame28"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame28"]["right_foot_index"]["x"]), 
                "y": float(sign["frame28"]["right_foot_index"]["y"]), 
                "z": float(sign["frame28"]["right_foot_index"]["z"])
            },
        },
                "frame29": {
            "nose": {
                "x": float(sign["frame29"]["nose"]["x"]), 
                "y": float(sign["frame29"]["nose"]["y"]), 
                "z": float(sign["frame29"]["nose"]["z"])
            },
            "left_eye_inner": {
                "x": float(sign["frame29"]["left_eye_inner"]["x"]), 
                "y": float(sign["frame29"]["left_eye_inner"]["y"]), 
                "z": float(sign["frame29"]["left_eye_inner"]["z"])
            },
            "left_eye": {
                "x": float(sign["frame29"]["left_eye"]["x"]), 
                "y": float(sign["frame29"]["left_eye"]["y"]), 
                "z": float(sign["frame29"]["left_eye"]["z"])
            },
            "left_eye_outer": {
                "x": float(sign["frame29"]["left_eye_outer"]["x"]), 
                "y": float(sign["frame29"]["left_eye_outer"]["y"]), 
                "z": float(sign["frame29"]["left_eye_outer"]["z"])
            },
            "right_eye_inner": {
                "x": float(sign["frame29"]["right_eye_inner"]["x"]), 
                "y": float(sign["frame29"]["right_eye_inner"]["y"]), 
                "z": float(sign["frame29"]["right_eye_inner"]["z"])
            },
            "right_eye": {
                "x": float(sign["frame29"]["right_eye"]["x"]), 
                "y": float(sign["frame29"]["right_eye"]["y"]), 
                "z": float(sign["frame29"]["right_eye"]["z"])
            },
            "right_eye_outer": {
                "x": float(sign["frame29"]["right_eye_outer"]["x"]), 
                "y": float(sign["frame29"]["right_eye_outer"]["y"]), 
                "z": float(sign["frame29"]["right_eye_outer"]["z"])
            },
            "left_ear": {
                "x": float(sign["frame29"]["left_ear"]["x"]), 
                "y": float(sign["frame29"]["left_ear"]["y"]), 
                "z": float(sign["frame29"]["left_ear"]["z"])
            },
            "right_ear": {
                "x": float(sign["frame29"]["right_ear"]["x"]), 
                "y": float(sign["frame29"]["right_ear"]["y"]), 
                "z": float(sign["frame29"]["right_ear"]["z"])
            },
            "mouth_left": {
                "x": float(sign["frame29"]["mouth_left"]["x"]), 
                "y": float(sign["frame29"]["mouth_left"]["y"]), 
                "z": float(sign["frame29"]["mouth_left"]["z"])
            },
            "mouth_right": {
                "x": float(sign["frame29"]["mouth_right"]["x"]), 
                "y": float(sign["frame29"]["mouth_right"]["y"]), 
                "z": float(sign["frame29"]["mouth_right"]["z"])
            },
            "left_shoulder": {
                "x": float(sign["frame29"]["left_shoulder"]["x"]), 
                "y": float(sign["frame29"]["left_shoulder"]["y"]), 
                "z": float(sign["frame29"]["left_shoulder"]["z"])
            },
            "right_shoulder": {
                "x": float(sign["frame29"]["right_shoulder"]["x"]), 
                "y": float(sign["frame29"]["right_shoulder"]["y"]), 
                "z": float(sign["frame29"]["right_shoulder"]["z"])
            },
            "left_elbow": {
                "x": float(sign["frame29"]["left_elbow"]["x"]), 
                "y": float(sign["frame29"]["left_elbow"]["y"]), 
                "z": float(sign["frame29"]["left_elbow"]["z"])
            },
            "right_elbow": {
                "x": float(sign["frame29"]["right_elbow"]["x"]), 
                "y": float(sign["frame29"]["right_elbow"]["y"]), 
                "z": float(sign["frame29"]["right_elbow"]["z"])
            },
            "left_wrist": {
                "x": float(sign["frame29"]["left_wrist"]["x"]), 
                "y": float(sign["frame29"]["left_wrist"]["y"]), 
                "z": float(sign["frame29"]["left_wrist"]["z"])
            },
            "right_wrist": {
                "x": float(sign["frame29"]["right_wrist"]["x"]), 
                "y": float(sign["frame29"]["right_wrist"]["y"]), 
                "z": float(sign["frame29"]["right_wrist"]["z"])
            },
            "left_pinky": {
                "x": float(sign["frame29"]["left_pinky"]["x"]), 
                "y": float(sign["frame29"]["left_pinky"]["y"]), 
                "z": float(sign["frame29"]["left_pinky"]["z"])
            },
            "right_pinky": {
                "x": float(sign["frame29"]["right_pinky"]["x"]), 
                "y": float(sign["frame29"]["right_pinky"]["y"]), 
                "z": float(sign["frame29"]["right_pinky"]["z"])
            },
            "left_index": {
                "x": float(sign["frame29"]["left_index"]["x"]), 
                "y": float(sign["frame29"]["left_index"]["y"]), 
                "z": float(sign["frame29"]["left_index"]["z"])
            },
            "right_index": {
                "x": float(sign["frame29"]["right_index"]["x"]), 
                "y": float(sign["frame29"]["right_index"]["y"]), 
                "z": float(sign["frame29"]["right_index"]["z"])
            },
            "left_thumb": {
                "x": float(sign["frame29"]["left_thumb"]["x"]), 
                "y": float(sign["frame29"]["left_thumb"]["y"]), 
                "z": float(sign["frame29"]["left_thumb"]["z"])
            },
            "right_thumb": {
                "x": float(sign["frame29"]["right_thumb"]["x"]), 
                "y": float(sign["frame29"]["right_thumb"]["y"]), 
                "z": float(sign["frame29"]["right_thumb"]["z"])
            },
            "left_hip": {
                "x": float(sign["frame29"]["left_hip"]["x"]), 
                "y": float(sign["frame29"]["left_hip"]["y"]), 
                "z": float(sign["frame29"]["left_hip"]["z"])
            },
            "right_hip": {
                "x": float(sign["frame29"]["right_hip"]["x"]), 
                "y": float(sign["frame29"]["right_hip"]["y"]), 
                "z": float(sign["frame29"]["right_hip"]["z"])
            },
            "left_knee": {
                "x": float(sign["frame29"]["left_knee"]["x"]), 
                "y": float(sign["frame29"]["left_knee"]["y"]), 
                "z": float(sign["frame29"]["left_knee"]["z"])
            },
            "right_knee": {
                "x": float(sign["frame29"]["right_knee"]["x"]), 
                "y": float(sign["frame29"]["right_knee"]["y"]), 
                "z": float(sign["frame29"]["right_knee"]["z"])
            },
            "left_ankle": {
                "x": float(sign["frame29"]["left_ankle"]["x"]), 
                "y": float(sign["frame29"]["left_ankle"]["y"]), 
                "z": float(sign["frame29"]["left_ankle"]["z"])
            },
            "right_ankle": {
                "x": float(sign["frame29"]["right_ankle"]["x"]), 
                "y": float(sign["frame29"]["right_ankle"]["y"]), 
                "z": float(sign["frame29"]["right_ankle"]["z"])
            },
            "left_heel": {
                "x": float(sign["frame29"]["left_heel"]["x"]), 
                "y": float(sign["frame29"]["left_heel"]["y"]), 
                "z": float(sign["frame29"]["left_heel"]["z"])
            },
            "right_heel": {
                "x": float(sign["frame29"]["right_heel"]["x"]), 
                "y": float(sign["frame29"]["right_heel"]["y"]), 
                "z": float(sign["frame29"]["right_heel"]["z"])
            },
            "left_foot_index": {
                "x": float(sign["frame29"]["left_foot_index"]["x"]), 
                "y": float(sign["frame29"]["left_foot_index"]["y"]), 
                "z": float(sign["frame29"]["left_foot_index"]["z"])
            },
            "right_foot_index": {
                "x": float(sign["frame29"]["right_foot_index"]["x"]), 
                "y": float(sign["frame29"]["right_foot_index"]["y"]), 
                "z": float(sign["frame29"]["right_foot_index"]["z"])
            },
        }
    }