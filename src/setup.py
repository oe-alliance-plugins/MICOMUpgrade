from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.MICOMUpgrade'
setup(name='enigma2-plugin-systemplugins-micomupgrade',
       version='3.0',
       description='micomupgrade',
       package_dir={pkg: 'MICOMUpgrade'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'buttons/*.png', 'wait.mvi', 'reboot.mvi']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
