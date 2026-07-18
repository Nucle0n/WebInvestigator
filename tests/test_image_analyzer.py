import unittest
from pathlib import Path

from lib.analyzer.image import find_matching_phashes
from lib.model.image import ImageInfo


def create_image(
    filename: str,
    phash: str | None,
) -> ImageInfo:
    """Create a minimal image model for analyzer tests."""

    path = Path(filename)

    return ImageInfo(
        path=path,
        relative_path=path,
        filename=filename,
        extension=".png",
        filesize=0,
        phash=phash,
    )


class FindMatchingPhashesTests(unittest.TestCase):
    def test_groups_connected_phashes_into_single_cluster(self) -> None:
        images = [
            create_image(
                "a.png",
                "0000000000000000",
            ),
            create_image(
                "b.png",
                "0000000000000003",
            ),
            create_image(
                "c.png",
                "000000000000000f",
            ),
        ]

        groups = find_matching_phashes(
            images,
            max_distance=2,
        )

        self.assertEqual(len(groups), 1)

        group = groups[0]

        self.assertEqual(
            [image.filename for image in group.images],
            [
                "a.png",
                "b.png",
                "c.png",
            ],
        )
        self.assertEqual(group.max_distance, 4)


if __name__ == "__main__":
    unittest.main()