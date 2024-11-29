class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.Median(nums1, nums2)  

    def Median(self, nums1, nums2):
        # Ініціалізуємо індекси
        i = 0  # Індекс для nums1
        j = 0  # Індекс для nums2
        count = 0  # Лічильник
        m1 = m2 = 0  # m1 та m2 зберігають останні два ел.

        # Загальна кількість
        size = len(nums1) + len(nums2)

        # Цикл триває
        while count < size // 2 + 1:
            # Зберігаємо попереднє значення m1 у m2
            m2 = m1

            # Порівнюємо поточні елементи
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    # Берем із nums1
                    m1 = nums1[i]
                    i += 1
                else:
                    # Берем із nums2
                    m1 = nums2[j]
                    j += 1
            elif i < len(nums1):
                m1 = nums1[i]
                i += 1
            elif j < len(nums2):
                m1 = nums2[j]
                j += 1

            # Збільшуємо
            count += 1

        # парна, повертаємо середнє
        if size % 2 == 0:
            return (m1 + m2) / 2
        else:
            # повертаємо
            return m1
