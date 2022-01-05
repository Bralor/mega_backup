import os

import pytest

from mega_backup.backup import BackupCreator


class TestBackUp:
    """Run testing functions that check creating archive."""

    def setup(self):
        name = "foobar"
        folders = [
            os.path.join("mega_backup/data", file)
            for file in os.listdir("mega_backup/data")
            if os.path.splitext(file)[1] == ".txt"
        ]
        self.testing_instance = BackupCreator(name, folders)

    def test_proper_instance_attributes(self):
        """Verify if the instance contains correct parameters."""
        assert self.testing_instance.folders != []

    def test_incorrect_parameters_in_testing_instance(self):
        """Verify if the instance contains correct parameters."""
        assert "incorrect_path" not in self.testing_instance.folders

    def test_correct_name_of_the_archive(self):
        """Check if the given parameter 'name'."""
        assert self.testing_instance.name == "foobar"

    def test_creating_name_of_the_archive(self):
        """Test to create a new archive name with given variables."""
        date = "11-11-2021"
        assert self.testing_instance.create_name(date) == "foobar-11-11-2021.tar"

    def test_write_new_tar_archive(self):
        """Check the creating of the new .tar archive file."""
        mod: str = "w:gz"
        self.testing_instance.write_archive("11-11-2011", mod)
        assert "foobar-11-11-2011.tar" in os.listdir()

    def test_write_incorrect_new_tar_archive(self):
        """Check the creating of the incorrect .tar archive file."""
        assert "foobar-12-12-2012.tar" not in os.listdir()

    def test_removing_tar_archive_after_uploading(self):
        """Check if the function correctly remove the archive."""
        assert self.testing_instance.remove_archive("foobar-11-11-2011.tar") == \
            "foobar-11-11-2011.tar successfully removed"

    def test_incorrect_removing_tar_archive_after_uploading(self):
        """
        Check if the function cannot remove the archive and return proper
        message.
        """
        assert self.testing_instance.remove_archive("foobar-11-11-2011.tar") == \
            "There is no such file, foobar-11-11-2011.tar"
