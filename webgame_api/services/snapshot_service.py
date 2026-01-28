# from parsers.age import parse_age
# from validation import age, snapshot
# from services.age_services import get_or_create_age
# from models.models import Country, Snapshot

parsed_age = parse_age()

if not validate_age(parsed_age):
    raise ValueError("Invalid age - mezihra")

age = get_or_create_age(parsed_age, db) # db is still not defined, why???

existing_snapshots = Snapshot.query.filter_by(
    country_id = country.id,
    age_id = age.id
).all()

if snapshot_validate(parsed_json, country.id, age.id, STATIC_KEYS, existing_snapshosts):
    snapshot = Snapshot(
        country_id = country.id,
        age_id = age.id,
        json_data = parsed_json,
        snapshot_hash = compute_snapshot_hash(
            prepare_snapshot_for_hash(parsed_json, STATIC_KEYS)
        )
    )
    
    db.sessions.add(snapshot)
    db.sessions.commit()