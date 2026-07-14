def format_size(size_bytes: int) -> str:
    """Convertit une taille en octets vers un format lisible."""
    units = ("o", "Ko", "Mo", "Go", "To")
    size = float(size_bytes)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size_bytes} o"