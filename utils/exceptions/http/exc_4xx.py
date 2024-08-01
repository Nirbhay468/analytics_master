import fastapi


async def http_404_exc_id_not_found_request(id: int) -> Exception:
    return fastapi.HTTPException(
        status_code=fastapi.status.HTTP_404_NOT_FOUND,
        detail=f"Either the brand with id `{id}` doesn't exist, has been deleted!"
    )
