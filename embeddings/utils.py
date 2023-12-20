import json
import hashlib

def short_md5(text):
    hash_obj = hashlib.md5(text.encode('utf-8'))
    hash_hex = hash_obj.hexdigest()
    return hash_hex[:8]

def load_json(fileName):
    return json.load(open(fileName,encoding='utf-8'))

def save_json(fileName,data):
    jfile = open(fileName, "w")
    jfile.write(json.dumps(data, indent=4))
    jfile.close()
    print(f"{len(data)} entries saved in {fileName}")
    return

def duration_text(duration):
    duration = abs(duration)
    milliseconds = int((duration - int(duration)) * 1000)
    seconds = int(duration) % 60
    minutes = (int(duration) // 60) % 60
    hours = (int(duration) // 60) // 60
    text = ""
    if(hours > 0):
        text += f"{hours} h "
    if(minutes > 0):
        text += f"{minutes} mn "
    if(seconds > 0):
        text += f"{seconds} s "
    if(milliseconds > 0):
        text += f"{milliseconds} ms "
    return text

def split_chunk(text, max_length, overlap):
    """
    Splits a text into chunks, each with a maximum length of max_length.
    Each chunk will overlap with the next by 'overlap' characters.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_length, len(text))
        if end < len(text):
            # Extend the chunk to include overlap, ensuring not to exceed text length
            overlap_end = min(end + overlap, len(text))
            chunk_end = text.rfind(' ', end, overlap_end)
            if chunk_end == -1 or chunk_end - start > max_length:
                # No space found in overlap range, or chunk too large, so use hard limit
                chunk_end = end
        else:
            chunk_end = end
        chunks.append(text[start:chunk_end])
        start = chunk_end
    return chunks

def split_chunk_text(text, max_length, overlap):
    """
    Splits a text into two sets of data:
    1. Chunks: Each with a maximum length of max_length, overlapping with the next by 'overlap' characters.
    2. Non-overlapping Texts: Corresponding segments of the chunks without any redundancy.
    """
    chunks = []
    non_overlapping_texts = []
    start = 0
    non_overlap_start = 0

    while start < len(text):
        end = min(start + max_length, len(text))
        chunk_end = end

        if end < len(text):
            # Extend the chunk to include overlap, ensuring not to exceed text length
            overlap_end = min(end + overlap, len(text))
            chunk_end = overlap_end

        # Append the chunk
        chunks.append(text[start:chunk_end])

        # Calculate non-overlapping text end
        # It should end where the next chunk will start
        non_overlap_end = min(start + max_length, len(text))

        # Append the non-overlapping text
        non_overlapping_texts.append(text[non_overlap_start:non_overlap_end])

        # Update the start for the next iteration
        start = non_overlap_end
        non_overlap_start = start

    combined_list = [{"chunk": chunk, "text": non_overlap_text} for chunk, non_overlap_text in zip(chunks, non_overlapping_texts)]
    return combined_list
