

from os import environ as osEnvironment

from pathlib import Path

from shutil import rmtree

from codeallybasic.UnitTestBase import UnitTestBase

from codeallybasic.ConfigurationLocator import XDG_CONFIG_HOME_ENV_VAR

from codeallybasic.ConfigurationProperties import ConfigurationProperties
from codeallybasic.ConfigurationProperties import ConfigurationNameValue
from codeallybasic.ConfigurationProperties import PropertyName
from codeallybasic.ConfigurationProperties import Section
from codeallybasic.ConfigurationProperties import SectionName
from codeallybasic.ConfigurationProperties import Sections
from codeallybasic.ConfigurationProperties import configurationGetter
from codeallybasic.ConfigurationProperties import configurationSetter

from unittest import TestSuite
from unittest import main as unitTestMain

BASE_FILE_NAME: str = 'FakeConfiguration.ini'
MODULE_NAME:    str = 'FakeModule'

#
#  TODO: Convert from list of ConfigurationNameValue to another dictionary
#
SECTION_OZZEE: Section = Section(
    [
        ConfigurationNameValue(name=PropertyName('ozzeeHairColor'),   defaultValue='Black'),
        ConfigurationNameValue(name=PropertyName('ozzeeDisposition'), defaultValue='Mean')
     ]
)

SECTION_FRAN: Section = Section(
    [
        ConfigurationNameValue(name=PropertyName('franHairColor'),   defaultValue='Blonde'),
        ConfigurationNameValue(name=PropertyName('franDisposition'), defaultValue='Funny')
     ]
)

SECTION_HASII: Section = Section(
    [
        ConfigurationNameValue(name=PropertyName('hasiiHairColor'),   defaultValue='Fake'),
        ConfigurationNameValue(name=PropertyName('hasiiDisposition'), defaultValue='Funky')
     ]
)

FAKE_SECTIONS: Sections = Sections(
    {
        SectionName('Ozzee'): SECTION_OZZEE,
        SectionName('Fran'):  SECTION_FRAN,
        SectionName('HASII'): SECTION_HASII,
    }
)


class FakeConfiguration(ConfigurationProperties):
    def __init__(self):
        super().__init__(baseFileName=BASE_FILE_NAME, moduleName=MODULE_NAME, sections=FAKE_SECTIONS)

    @property
    @configurationGetter(sectionName='Ozzee')
    def ozzeeHairColor(self) -> str:
        return ''

    @ozzeeHairColor.setter
    @configurationSetter(sectionName='Ozzee')
    def ozzeeHairColor(self, newValue: str):
        pass


class TestConfigurationProperties(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo – Humberto A. Sanchez II
        Generated: 14 February 2024
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()
        """
        Create a fake location since we know that the configuration
        locator favors using the XDG environment variable
        """
        fakeXDGPATH: Path = Path('/tmp/fakeXDG/.config')

        osEnvironment[XDG_CONFIG_HOME_ENV_VAR] = fakeXDGPATH.as_posix()
        self._fakeConfig: FakeConfiguration = FakeConfiguration()

    def tearDown(self):
        super().tearDown()
        configurationFile: Path = self._fakeConfig.fileName
        configurationFile.unlink(missing_ok=True)

        modulePart: Path = configurationFile.parents[0]
        modulePart.rmdir()

        configPart: Path = modulePart.parents[0]
        rmtree(configPart)
        finalPart: Path = configPart.parents[0]
        rmtree(finalPart)

    def testFileCreation(self):

        self.assertTrue(self._fakeConfig.fileName.exists(), f'Missing: {self._fakeConfig.fileName}')

    def testPropertySet(self):

        self.assertEqual('Black', self._fakeConfig.ozzeeHairColor, 'initial value')
        self._fakeConfig.ozzeeHairColor = 'Blue'

        self.assertEqual('Blue', self._fakeConfig.ozzeeHairColor, 'changed value')

        self.logger.info(f'{self._fakeConfig.ozzeeHairColor=}')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestConfigurationProperties))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
